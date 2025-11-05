from __future__ import annotations

from functools import wraps
from typing import Any, Dict, Optional

from flask import (
    Flask,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from .domain import ALL_DIMENSIONS, DIMENSION_DETAILS, MANAGEMENT_LEVELS, summarize_by_category
from .services import (
    Assessment,
    InsightService,
    User,
    create_assessment,
    delete_assessment,
    ensure_seed_users,
    find_assessment,
    get_all_assessments,
    get_insight_service,
    update_assessment,
    verify_user,
)


def configure_routes(app: Flask) -> None:
    ensure_seed_users()

    def current_user() -> Optional[User]:
        email = session.get("user_email")
        role = session.get("user_role")
        if not email or not role:
            return None
        return User(id="", email=email, password_hash="", role=role)

    def login_required(view):
        @wraps(view)
        def wrapped(*args, **kwargs):
            if not current_user():
                return redirect(url_for("login"))
            return view(*args, **kwargs)

        return wrapped

    @app.route("/login", methods=["GET", "POST"])
    def login():
        if request.method == "POST":
            email = request.form.get("email", "")
            password = request.form.get("password", "")
            user = verify_user(email, password)
            if user:
                session["user_email"] = user.email
                session["user_role"] = user.role
                flash("Dobrodošli natrag!", "success")
                return redirect(url_for("dashboard"))
            flash("Neuspješna prijava. Provjerite podatke.", "danger")
        return render_template("login.html")

    @app.route("/logout")
    def logout():
        session.clear()
        flash("Odjavljeni ste.", "info")
        return redirect(url_for("login"))

    @app.route("/")
    @login_required
    def dashboard():
        user = current_user()
        assert user is not None
        assessments = get_all_assessments()
        if not user.is_master:
            assessments = [a for a in assessments if a.assessed_by == user.email]
        summary = summarize_by_category([a.to_dict() for a in assessments])
        return render_template(
            "dashboard.html",
            user=user,
            assessments=assessments,
            summary=summary,
            show_assessed_by=user.is_master,
        )

    def _parse_assessment_form(existing: Optional[Assessment] = None) -> Dict[str, Any]:
        result: Dict[str, Any] = {
            "full_name": request.form.get("full_name", existing.full_name if existing else ""),
            "position": request.form.get("position", existing.position if existing else ""),
            "management_level": request.form.get(
                "management_level", existing.management_level if existing else ""
            ),
        }
        for dimension in ALL_DIMENSIONS:
            key = f"dimension_{dimension}"
            if key in request.form:
                result[dimension] = int(request.form.get(key, 1))
            elif existing:
                result[dimension] = existing.dimensions.get(dimension, 1)
        return result

    @app.route("/assessment/new", methods=["GET", "POST"])
    @login_required
    def create_assessment_view():
        user = current_user()
        assert user is not None
        if request.method == "POST":
            data = _parse_assessment_form()
            for dimension in ALL_DIMENSIONS:
                if dimension not in data:
                    flash("Molimo unesite sve ocjene.", "danger")
                    break
            else:
                create_assessment(data, user)
                flash("Procjena je spremljena.", "success")
                return redirect(url_for("dashboard"))
        return render_template(
            "assessment_form.html",
            user=user,
            assessment=None,
            dimensions=DIMENSION_DETAILS,
            management_levels=MANAGEMENT_LEVELS,
        )

    @app.route("/assessment/<assessment_id>/edit", methods=["GET", "POST"])
    @login_required
    def edit_assessment_view(assessment_id: str):
        user = current_user()
        assert user is not None
        assessment = find_assessment(assessment_id)
        if not assessment:
            flash("Procjena nije pronađena.", "danger")
            return redirect(url_for("dashboard"))
        if assessment.assessed_by != user.email and not user.is_master:
            flash("Nemate ovlasti za uređivanje ove procjene.", "danger")
            return redirect(url_for("dashboard"))
        if request.method == "POST":
            data = _parse_assessment_form(existing=assessment)
            updated = update_assessment(assessment_id, data, user)
            if updated:
                flash("Procjena je ažurirana.", "success")
                return redirect(url_for("dashboard"))
            flash("Nije moguće ažurirati procjenu.", "danger")
        return render_template(
            "assessment_form.html",
            user=user,
            assessment=assessment,
            dimensions=DIMENSION_DETAILS,
            management_levels=MANAGEMENT_LEVELS,
        )

    @app.route("/assessment/<assessment_id>/delete", methods=["POST"])
    @login_required
    def delete_assessment_view(assessment_id: str):
        user = current_user()
        assert user is not None
        if delete_assessment(assessment_id, user):
            flash("Procjena je izbrisana.", "info")
        else:
            flash("Brisanje nije dopušteno.", "danger")
        return redirect(url_for("dashboard"))

    @app.route("/visualizations")
    @login_required
    def visualizations():
        user = current_user()
        assert user is not None
        mode = request.args.get("mode", "matrix")
        selected_id = request.args.get("selected")
        comparison_a = request.args.get("a")
        comparison_b = request.args.get("b")
        all_assessments = get_all_assessments()
        if not user.is_master:
            all_assessments = [a for a in all_assessments if a.assessed_by == user.email]
        selected_assessment = (
            find_assessment(selected_id) if selected_id else (all_assessments[0] if all_assessments else None)
        )
        if selected_assessment and not user.is_master and selected_assessment.assessed_by != user.email:
            selected_assessment = None
        comparison_first = find_assessment(comparison_a) if comparison_a else None
        comparison_second = find_assessment(comparison_b) if comparison_b else None
        if comparison_first and not (user.is_master or comparison_first.assessed_by == user.email):
            comparison_first = None
        if comparison_second and not (user.is_master or comparison_second.assessed_by == user.email):
            comparison_second = None
        return render_template(
            "visualizations.html",
            user=user,
            mode=mode,
            assessments=all_assessments,
            selected=selected_assessment,
            comparison_a=comparison_first,
            comparison_b=comparison_second,
            dimensions=DIMENSION_DETAILS,
        )

    @app.route("/api/assessments")
    @login_required
    def api_assessments():
        user = current_user()
        assert user is not None
        assessments = get_all_assessments()
        if not user.is_master:
            assessments = [a for a in assessments if a.assessed_by == user.email]
        return jsonify([a.to_dict() for a in assessments])

    @app.route("/api/assessments/<assessment_id>")
    @login_required
    def api_assessment_detail(assessment_id: str):
        user = current_user()
        assert user is not None
        assessment = find_assessment(assessment_id)
        if not assessment:
            return jsonify({"error": "Not found"}), 404
        if not user.is_master and assessment.assessed_by != user.email:
            return jsonify({"error": "Forbidden"}), 403
        return jsonify(assessment.to_dict())

    @app.route("/api/insights/<assessment_id>")
    @login_required
    def api_insights(assessment_id: str):
        user = current_user()
        assert user is not None
        assessment = find_assessment(assessment_id)
        if not assessment:
            return jsonify({"error": "Not found"}), 404
        if not user.is_master and assessment.assessed_by != user.email:
            return jsonify({"error": "Forbidden"}), 403
        insight_service: InsightService = get_insight_service()
        content = insight_service.generate_insight(assessment)
        return jsonify({"content": content})


__all__ = ["configure_routes"]
