from flask import Blueprint
from flask import render_template, request, redirect, url_for

from models.models import Jogo
from database import db

jogos_bp = Blueprint('jogos', __name__)

@jogos_bp.route('/jogos', methods=['GET'])
def listar_jogos():

    jogos = db.session.scalars(
        db.select(Jogo)
    ).all()

    return render_template("jogos/listar.html", jogos=jogos)

@jogos_bp.route('/jogos/<int:id>', methods=['GET'])
def detalhar_jogo(id):

    jogos = db.get_or_404(Jogo, id)

    return render_template('jogos/detalhes.html', jogos=jogos)

@jogos_bp.route('/jogos/novo', methods=['POST'])
def novo_jogo():

    if request.method == 'POST':

        jogo = Jogo(
            titulo = request.form['titulo'],
        )

        db.session.add(jogo)
        db.session.commit()

        return redirect(url_for('jogos.listar_jogos'))

    return render_template("jogos/formulario.html")

@jogos_bp.route('/jogos/<int:id>/editar', methods=['GET, POST'])
def editar_jogo(id):

    jogo = db.get_or_404(Jogo, id)

    if request.method == 'POST':
        jogo.titulo = request.form['titulo']

        db.session.commit()

        return redirect(url_for('jogos.listar_jogos'))

    return render_template("jogos/formulario.html")

@jogos_bp.route('/jogos/<int:id>/excluir', methods=['DELETE'])
def excluir_jogo(id):

    jogo = db.get_or_404(Jogo, id)

    db.session.delete(jogo)
    db.session.commit()

    return redirect(url_for('jogos.listar_jogos'))