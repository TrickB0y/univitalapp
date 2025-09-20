from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from univitalapp.contas import login_requirido  # type: ignore

bp = Blueprint("diario", __name__, url_prefix="diario/")

@bp.route("/", methods=("GET", "POST"))
@login_requirido
def index():
    return render_template("app/diario.html")