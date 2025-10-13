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
    diario_feito = False

    db = get_db()
    diario = db.execute(
        'SELECT max(data_diario) as data_diario FROM Diarios WHERE id_usuario = ?',
        (g.usuario['id'],)
    ).fetchone()
    data_diario = None

    if diario["data_diario"] is not None:
        data_diario = date.fromisoformat(diario["data_diario"])
    if data_diario == date.today():
        diario_feito = True
        

    return render_template("menu.html", diario_feito = diario_feito)