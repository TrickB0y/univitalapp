from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from datetime import date

from univitalapp.contas import login_requirido  # type: ignore
from univitalapp.database import get_db # type: ignore

bp = Blueprint("menu", __name__, url_prefix="/")

@bp.route("/", methods=("GET",))
@login_requirido
def index():
    erro = None

    return render_template("menu.html")