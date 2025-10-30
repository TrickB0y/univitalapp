from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from univitalapp.contas import login_requirido # type: ignore

bp = Blueprint("tcc", __name__, url_prefix="/tcc")

@bp.route("/", methods=("GET",))
@login_requirido
def index():
    return render_template("app/tcc/menu.html")

@bp.route("/fazer/1", methods=("GET",))
@login_requirido
def tcc1():
    return render_template("app/tcc/terapia/tcc1.html")

@bp.route("/fazer/2", methods=("GET",))
@login_requirido
def tcc2():
    return render_template("app/tcc/terapia/tcc2.html")

@bp.route("/fazer/3", methods=("GET",))
@login_requirido
def tcc3():
    return render_template("app/tcc/terapia/tcc3.html")

@bp.route("/fazer/4", methods=("GET",))
@login_requirido
def tcc4():
    return render_template("app/tcc/terapia/tcc4.html")