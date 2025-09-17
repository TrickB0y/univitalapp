from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint("inicio", __name__, url_prefix="/boas-vindas")

@bp.route("/", methods=("GET",))
def boas_vindas():
    user_id = session.get("user_id")
    if user_id != None:
        return redirect(url_for("index"))
    return render_template("boas_vindas.html")