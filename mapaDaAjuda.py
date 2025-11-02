from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from univitalapp.contas import login_requirido # type: ignore

bp = Blueprint("mapa-da-ajuda", __name__, url_prefix="/mapa-da-ajuda")

@bp.route("/", methods=("GET",))
@login_requirido
def index():
    return render_template("app/mapa-da-ajuda/index.html")