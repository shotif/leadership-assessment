from __future__ import annotations

import os
import uuid
from dataclasses import dataclass
from typing import Dict, List, Optional

from werkzeug.security import check_password_hash, generate_password_hash

from . import storage
from .domain import ALL_DIMENSIONS, DIMENSION_DETAILS, calculate_scores


@dataclass
class User:
    id: str
    email: str
    password_hash: str
    role: str  # "standard" or "master"

    @property
    def is_master(self) -> bool:
        return self.role == "master"


def _deserialize_user(data: Dict) -> User:
    return User(
        id=data["id"],
        email=data["email"],
        password_hash=data["password_hash"],
        role=data.get("role", "standard"),
    )


def _serialize_user(user: User) -> Dict:
    return {
        "id": user.id,
        "email": user.email,
        "password_hash": user.password_hash,
        "role": user.role,
    }


def get_all_users() -> List[User]:
    return [_deserialize_user(u) for u in storage.load_users()]


def find_user_by_email(email: str) -> Optional[User]:
    email = email.lower().strip()
    for user in get_all_users():
        if user.email.lower() == email:
            return user
    return None


def verify_user(email: str, password: str) -> Optional[User]:
    user = find_user_by_email(email)
    if user and check_password_hash(user.password_hash, password):
        return user
    return None


def create_user(email: str, password: str, role: str = "standard") -> User:
    user = User(
        id=str(uuid.uuid4()),
        email=email.strip(),
        password_hash=generate_password_hash(password),
        role=role,
    )
    users = [_serialize_user(u) for u in get_all_users()] + [_serialize_user(user)]
    storage.save_users(users)
    return user


def ensure_seed_users() -> None:
    users = get_all_users()
    if users:
        return
    default_password = os.environ.get("LEADERSHIP_APP_DEFAULT_PASSWORD", "ChangeMe123!")
    master_email = os.environ.get("LEADERSHIP_APP_MASTER_EMAIL", "master@example.com")
    standard_email = os.environ.get("LEADERSHIP_APP_STANDARD_EMAIL", "user@example.com")
    create_user(master_email, default_password, role="master")
    create_user(standard_email, default_password, role="standard")


@dataclass
class Assessment:
    id: str
    assessed_by: str
    full_name: str
    position: str
    management_level: str
    dimensions: Dict[str, int]
    adequacy: float
    potential: float
    category: str

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "assessed_by": self.assessed_by,
            "full_name": self.full_name,
            "position": self.position,
            "management_level": self.management_level,
            "dimensions": self.dimensions,
            "adequacy": self.adequacy,
            "potential": self.potential,
            "category": self.category,
        }


def _deserialize_assessment(data: Dict) -> Assessment:
    return Assessment(
        id=data["id"],
        assessed_by=data.get("assessed_by", ""),
        full_name=data.get("full_name", ""),
        position=data.get("position", ""),
        management_level=data.get("management_level", ""),
        dimensions=data.get("dimensions", {}),
        adequacy=data.get("adequacy", 0.0),
        potential=data.get("potential", 0.0),
        category=data.get("category", "Eliminirati"),
    )


def _serialize_assessment(assessment: Assessment) -> Dict:
    return assessment.to_dict()


def get_all_assessments() -> List[Assessment]:
    return [_deserialize_assessment(a) for a in storage.load_assessments()]


def save_assessments(assessments: List[Assessment]) -> None:
    storage.save_assessments([_serialize_assessment(a) for a in assessments])


def create_assessment(data: Dict, user: User) -> Assessment:
    dimensions = {dim: int(data.get(dim, 1)) for dim in ALL_DIMENSIONS}
    scores = calculate_scores(dimensions)
    assessment = Assessment(
        id=str(uuid.uuid4()),
        assessed_by=user.email,
        full_name=data.get("full_name", "").strip(),
        position=data.get("position", "").strip(),
        management_level=data.get("management_level", "").strip(),
        dimensions=dimensions,
        adequacy=scores["adequacy"],
        potential=scores["potential"],
        category=scores["category"],
    )
    existing = get_all_assessments()
    existing.append(assessment)
    save_assessments(existing)
    return assessment


def update_assessment(assessment_id: str, data: Dict, user: User) -> Optional[Assessment]:
    assessments = get_all_assessments()
    for idx, assessment in enumerate(assessments):
        if assessment.id == assessment_id:
            if assessment.assessed_by != user.email and not user.is_master:
                return None
            dimensions = {dim: int(data.get(dim, 1)) for dim in ALL_DIMENSIONS}
            scores = calculate_scores(dimensions)
            assessment.full_name = data.get("full_name", assessment.full_name).strip()
            assessment.position = data.get("position", assessment.position).strip()
            assessment.management_level = data.get("management_level", assessment.management_level).strip()
            assessment.dimensions = dimensions
            assessment.adequacy = scores["adequacy"]
            assessment.potential = scores["potential"]
            assessment.category = scores["category"]
            assessments[idx] = assessment
            save_assessments(assessments)
            return assessment
    return None


def delete_assessment(assessment_id: str, user: User) -> bool:
    assessments = get_all_assessments()
    new_assessments: List[Assessment] = []
    removed = False
    for assessment in assessments:
        if assessment.id == assessment_id:
            if assessment.assessed_by != user.email and not user.is_master:
                return False
            removed = True
            continue
        new_assessments.append(assessment)
    if removed:
        save_assessments(new_assessments)
    return removed


def find_assessment(assessment_id: str) -> Optional[Assessment]:
    for assessment in get_all_assessments():
        if assessment.id == assessment_id:
            return assessment
    return None


class InsightService:
    def __init__(self):
        self.api_key = os.environ.get("GOOGLE_GEMINI_API_KEY")

    def generate_insight(self, assessment: Assessment) -> str:
        if not self.api_key:
            return (
                "AI uvid nije generiran jer Google Gemini API ključ nije konfiguriran. "
                "Postavite varijablu okoline GOOGLE_GEMINI_API_KEY kako biste omogućili ovu značajku."
            )
        try:
            import google.generativeai as genai  # type: ignore

            genai.configure(api_key=self.api_key)
            prompt = self._build_prompt(assessment)
            model_name = os.environ.get("GOOGLE_GEMINI_MODEL", "models/gemini-1.5-flash")
            response = genai.GenerativeModel(model_name).generate_content(prompt)
            return response.text or "Nije moguće generirati uvid u ovom trenutku."
        except Exception as exc:  # pragma: no cover - integration fallback
            return f"Generiranje AI uvida nije uspjelo: {exc}"

    def _build_prompt(self, assessment: Assessment) -> str:
        lines = [
            "Analiziraj profil vodstva u nastavku i izradi sažetak na hrvatskom jeziku.",
            "Uključi odjeljke: Sažetak, Ključne snage, Razvojna područja.",
            "Koristi profesionalan i konstruktivan ton.",
            "",  # blank line
            f"Ime i prezime: {assessment.full_name}",
            f"Pozicija: {assessment.position}",
            f"Razina menadžmenta: {assessment.management_level}",
            f"Ocjena adekvatnosti: {assessment.adequacy}",
            f"Ocjena potencijala: {assessment.potential}",
            f"Kategorija: {assessment.category}",
            "", "Ocjene po dimenzijama:",
        ]
        for dim in ALL_DIMENSIONS:
            detail = DIMENSION_DETAILS[dim]
            score = assessment.dimensions.get(dim)
            label = detail.scale.get(score, str(score))
            behavior = detail.description.get(score, "")
            lines.append(f"- {detail.name} ({detail.group}): {score} - {label}. {behavior}")
        return "\n".join(lines)


def get_insight_service() -> InsightService:
    return InsightService()
