from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from datetime import (date, timedelta)
from univitalapp.contas import login_requirido # type: ignore
from univitalapp.database import get_db # type: ignore

bp = Blueprint("questionario", __name__, url_prefix="/questionario")

@bp.route("/", methods=("GET",))
@login_requirido
def index():
    db = get_db()

    questionario = db.execute(
        'SELECT * FROM RespostasQuestionario WHERE id_usuario = ? ORDER BY rowid DESC LIMIT 1',
        (g.usuario['id'],)
    ).fetchone()
    data_questionario = None
    erro = None

    questionario_feito = False

    completo = False
    if questionario != None:
        respondidas = 0
        for i in range(1, 31):
            if questionario['resposta_questao_' + str(i)] != None:
                respondidas += 1
    
        if respondidas == 30:
            completo = True

        if completo:
            data_questionario = questionario['data_questionario']
            data_liberada = None
            trintadias = timedelta(days= 30)
            data_liberada = data_questionario + trintadias
            presente = date.today()
            if data_liberada > presente:
                questionario_feito = True
                
    return render_template("app/questionario/menu.html", questionario_feito = questionario_feito)

@bp.route("/historico", methods=("GET",))
@login_requirido
def historico():
    itens = []
    db = get_db()
    respostas = db.execute(
        "SELECT * FROM RespostasQuestionario WHERE id_usuario = ?",
        (g.usuario['id'],)
    ).fetchall()

    for i in respostas:
        respondidas = 0
        completo = False
        for j in range(1, 31):
            if i['resposta_questao_' + str(j)] != None:
                respondidas += 1
    
            if respondidas == 30:
                completo = True
            
            lista = [i]

            if completo:
                itens += lista

    return render_template("app/questionario/historico.html", completos = itens)

@bp.route("/resultado/<id>")
@login_requirido
def resultado(id):
    idint = int(id)
    db = get_db()
    respostas = db.execute(
        "SELECT * FROM RespostasQuestionario WHERE id = ? AND id_usuario = ?",
        (idint, g.usuario['id'],)
    ).fetchone()
    if respostas == None:
        return redirect(url_for('questionario.index'))
    else:
        respondidas = 0
        completo = False
        for i in range(1, 31):
            if respostas['resposta_questao_' + str(i)] != None:
                respondidas += 1
    
        if respondidas == 30:
            completo = True
        
        if not completo:
            return redirect(url_for('questionario.index'))
    
    pontuação = 0
    risco = None
    texto = None
    data = respostas['data_questionario'].strftime("%d/%m/%Y")
    for i in range(1, 31):
        pontuação += respostas['resposta_questao_' + str(i)] - 1

    if pontuação <= 29:
        risco = "Baixo"
        texto = ["Indica poucos sinais de preocupação. Há hábitos que podem ser melhorados, mas não sugerem risco significativo de transtornos alimentares.",
                "Foco em educação alimentar e autoconhecimento."]
    elif pontuação >= 30 and pontuação <= 59:
        risco = "Leve"
        texto = ["Mostra alguns comportamentos alimentares ou emocionais que merecem atenção. Pode ser um estágio inicial de relação conflituosa com a comida e o corpo.", 
                "Intervenção precoce com orientações de nutricionista e acompanhamento leve de saúde mental."]
    elif pontuação >= 60 and pontuação <= 89:
        risco = "Moderado"
        texto = ["Sugere comportamentos e pensamentos consistentes com possíveis transtornos alimentares. Já pode haver impacto no bem-estar físico e emocional. Procura de acompanhamento profissional é altamente recomendada.",
                 "Encaminhar para avaliação profissional imediata (nutricionista + psicólogo/psiquiatra)."]
    elif pontuação >= 90 and pontuação <= 120:
        risco = "Alto"
        texto = ["Sinais fortes de possível transtorno alimentar, com impacto significativo na saúde física, emocional e social. É fundamental buscar acompanhamento com nutricionista e psicólogo especializados em transtornos alimentares.",
                 "Encaminhar para avaliação profissional imediata (nutricionista + psicólogo/psiquiatra)."]


    return render_template("app/questionario/resultado.html", data = data, risco = risco, texto = texto)


@bp.route("fazer/<id>", methods=("GET", "POST"))
@login_requirido
def questionario(id):
    idint = int(id)
    if idint < 1 or idint > 30:
        redirect(url_for("questionario.index"))
    db = get_db()

    questionario = db.execute(
        'SELECT * FROM RespostasQuestionario WHERE id_usuario = ? ORDER BY rowid DESC LIMIT 1',
        (g.usuario['id'],)
    ).fetchone()
    data_questionario = None
    erro = None

    completo = False
    if questionario != None:
        respondidas = 0
        for i in range(1, 31):
            if questionario['resposta_questao_' + str(i)] != None:
                respondidas += 1
    
        if respondidas == 30:
            completo = True

        if completo:
            data_questionario = questionario['data_questionario']
            data_liberada = None
            trintadias = timedelta(days= 30)
            data_liberada = data_questionario + trintadias
            presente = date.today()
            if data_liberada > presente:
                return redirect(url_for('questionario.index'))
    
    if request.method == "POST":
        resposta = request.form["resposta"]
        resposta_id = 0

        if resposta != "nunca" and resposta != "raramente" and resposta != "as-vezes" and resposta != "frequentemente" and resposta != "sempre":
            erro = "resposta desconhecido."
        elif resposta == "nunca":
            resposta_id = 1
        elif resposta == "raramente":
            resposta_id = 2
        elif resposta == "as-vezes":
            resposta_id = 3
        elif resposta == "frequentemente":
            resposta_id = 4
        elif resposta == "sempre":
            resposta_id = 5
        
        if erro:
            flash(erro)
        else:
            questionario2 = db.execute(
                "SELECT * FROM RespostasQuestionario WHERE id_usuario = ? ORDER BY rowid DESC LIMIT 1",
                (g.usuario['id'],)
            ).fetchone()

            completo2 = False
            if questionario2 != None:
                respondidas2 = 0
                for i in range(1, 31):
                    if questionario['resposta_questao_' + str(i)] != None:
                        respondidas2 += 1
    
                if respondidas == 30:
                    completo2 = True

            if questionario2 != None and not completo2 and respondidas2 > 0:
                db.execute(
                    "UPDATE RespostasQuestionario SET resposta_questao_" + str(id) + " = ? WHERE id = ?",
                    (resposta_id, questionario2['id'])
                )
                db.commit()
                if idint < 30:
                    return redirect(url_for("questionario.questionario", id = idint + 1))
                elif idint == 30:
                    return redirect(url_for("questionario.resultado", id = questionario2['id']))
            else:
                db.execute(
                    "INSERT INTO RespostasQuestionario(id_usuario, resposta_questao_" + str(id) + ") VALUES (?, ?)",
                    (g.usuario['id'], resposta_id)
                )
                db.commit()
                return redirect(url_for("questionario.questionario", id = idint + 1))
    
    pergunta = db.execute(
        "SELECT texto FROM PerguntasQuestionario WHERE id = ?",
        (idint,)
    ).fetchone()

    return render_template("app/questionario/questionario.html", texto = pergunta['texto'])