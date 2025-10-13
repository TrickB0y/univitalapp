from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from datetime import date

from univitalapp.contas import login_requirido # type: ignore
from univitalapp.database import get_db # type: ignore

bp = Blueprint("diario", __name__, url_prefix="/diario")

@bp.route("/", methods=("GET", "POST"))
@login_requirido
def index():
    db = get_db()
    diario = db.execute(
        'SELECT max(data_diario) as data_diario FROM Diarios WHERE id_usuario = ?',
        (g.usuario['id'],)
    ).fetchone()
    data_diario = None
    erro = None

    if diario["data_diario"] is not None:
        data_diario = date.fromisoformat(diario["data_diario"])
    if data_diario == date.today():
        return redirect(url_for("menu.index"))

    if request.method == "POST":
        sentimento = request.form["sentimento"]
        texto = request.form["detalhes"]
        sentimento_id = 0

        if sentimento != "raiva" and sentimento != "tristeza" and sentimento != "felicidade" and sentimento != "medo" and sentimento != "frustacao":
            erro = "Sentimento desconhecido."
        elif sentimento == "raiva":
            sentimento_id = 1
        elif sentimento == "tristeza":
            sentimento_id = 2
        elif sentimento == "felicidade":
            sentimento_id = 3
        elif sentimento == "medo":
            sentimento_id = 4
        elif sentimento == "frustacao":
            sentimento_id = 5
        
        if erro is None:
            db.execute(
                "INSERT INTO Diarios(id_usuario, id_sentimento, texto) VALUES (?, ?, ?)",
                (g.usuario['id'], sentimento_id, texto)
            )
            db.commit()
            return redirect(url_for("menu.index"))

        flash(erro)

    return render_template("app/diario.html")