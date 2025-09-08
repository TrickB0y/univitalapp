import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from univitalapp.database import get_db # type: ignore



bp = Blueprint("auth", __name__, url_prefix="/auth")

# página do registro
@bp.route("/registro", methods=("GET", "POST"))
def registro():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]
        senha_confirmacao = request.form["senha_confirmacao"]
        nome  = request.form["nome"]
        sobrenome = request.form["sobrenome"]
        telefone = request.form["telefone"]
        db = get_db()
        erro = None
        
        if not email:
            erro = "O email é obrigatório."
        elif not senha:
            erro = "A senha é obrigatória."
        elif not senha_confirmacao:
            erro = "A senha deve ser confirmada."
        elif not nome:
            erro = "O nome é obrigatório."
        elif not sobrenome:
            erro = "O sobrenome é obrigatório."
        elif not telefone:
            erro = "O telefone é obrigatório."    
        elif senha != senha_confirmacao:
            erro = "As senhas não são iguais."
            
        if erro is None:
            try:
                db.execute(
                    "INSERT INTO Usuarios (email, senha, nome, sobrenome, telefone) VALUES (?, ?, ?, ?, ?)",
                    (email, generate_password_hash(senha), nome, sobrenome, telefone),
                ).commit()
            except db.IntegrityError:
                erro = f"O Email {email} já esta cadastrado."
            else:
                return redirect(url_for("auth.login"))
        # a função flash manda uma mensagem para o template de html em tempo de execução pro usuario.
        # neste caso estamos mandando o erro cometido pelo usario no cadastro
        flash(erro)
        
    return render_template("auth/registro.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]
        db = get_db()
        erro = None
        
        usuario = db.execute(
            "SELECT * FROM Usuarios WHERE email = ?", (email,)
        ).fetchone()
        
        if usuario is None:
            erro = "O email está incorreto."
        elif not check_password_hash(usuario["senha"], senha):
            erro = "A senha está incorreta."
            
        if erro is None:
            session.clear()
            session["user_id"] = usuario["id"]
            return redirect(url_for("index"))
        
        flash(erro)
        
    return render_template("auth/login.html")    
    

# to do: pagina de login

# to do: função de sessão logada

# to do: função de log out

# to do: função de login obrigatorio