import json
import threading
from pathlib import Path
from typing import Dict, List


_DATA_DIR = Path(__file__).resolve().parent / "data"
_ASSESSMENTS_FILE = _DATA_DIR / "assessments.json"
_USERS_FILE = _DATA_DIR / "users.json"
_LOCK = threading.Lock()


def _ensure_data_files() -> None:
    _DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not _ASSESSMENTS_FILE.exists():
        _ASSESSMENTS_FILE.write_text(json.dumps({"assessments": []}, indent=2), encoding="utf-8")
    if not _USERS_FILE.exists():
        _USERS_FILE.write_text(json.dumps({"users": []}, indent=2), encoding="utf-8")


def load_assessments() -> List[Dict]:
    _ensure_data_files()
    with _ASSESSMENTS_FILE.open("r", encoding="utf-8") as f:
        return json.load(f).get("assessments", [])


def save_assessments(assessments: List[Dict]) -> None:
    _ensure_data_files()
    with _LOCK:
        with _ASSESSMENTS_FILE.open("w", encoding="utf-8") as f:
            json.dump({"assessments": assessments}, f, indent=2, ensure_ascii=False)


def load_users() -> List[Dict]:
    _ensure_data_files()
    with _USERS_FILE.open("r", encoding="utf-8") as f:
        return json.load(f).get("users", [])


def save_users(users: List[Dict]) -> None:
    _ensure_data_files()
    with _LOCK:
        with _USERS_FILE.open("w", encoding="utf-8") as f:
            json.dump({"users": users}, f, indent=2, ensure_ascii=False)
