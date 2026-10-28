from flask import Blueprint
from flask import render_template, request, redirect, url_for, abort
from sqlalchemy import select

from models.models import Jogo, Desenvolvedora
from database import Session

jogos_bp = Blueprint('jogos', __name__)

@jogos_bp.route('/jogos', methods=['GET'])
def listar_jogos():

    with Session() as session:
        jogos = session.scalars(select(Jogo)).all()

        return render_template("jogos/listar.html", jogos=jogos)

@jogos_bp.route('/jogos/<int:id>', methods=['GET'])
def detalhar_jogo(id):

    with Session() as session:
        jogo = session.get(Jogo, id)

        if jogo is None:
            abort(404)

        return render_template('jogos/detalhes.html', jogo=jogo)

@jogos_bp.route('/jogos/novo', methods=['GET', 'POST'])
def novo_jogo():

    with Session() as session:
        if request.method == 'POST':
            titulo = request.form.get('titulo', '').strip()
            desenvolvedora_id = request.form.get('desenvolvedora_id', type=int)

            if not titulo or desenvolvedora_id is None:
                abort(400)

            if session.get(Desenvolvedora, desenvolvedora_id) is None:
                abort(400)

            jogo = Jogo(titulo = titulo, desenvolvedora_id = desenvolvedora_id)

            session.add(jogo)
            session.commit()

            return redirect(url_for('jogos.listar_jogos'))

        desenvolvedoras = session.scalars(select(Desenvolvedora)).all()

        return render_template("jogos/formulario.html", jogo=None,
                               desenvolvedoras=desenvolvedoras, titulo="Cadastrar jogo",
                               acao=url_for('jogos.novo_jogo'))

@jogos_bp.route('/jogos/<int:id>/editar', methods=['GET', 'POST'])
def editar_jogo(id):

    with Session() as session:
        jogo = session.get(Jogo, id)

        if jogo is None:
            abort(404)

        if request.method == 'POST':
            titulo = request.form.get('titulo', '').strip()
            desenvolvedora_id = request.form.get('desenvolvedora_id', type=int)

            if not titulo or desenvolvedora_id is None:
                abort(400)

            if session.get(Desenvolvedora, desenvolvedora_id) is None:
                abort(400)

            jogo.titulo = titulo
            jogo.desenvolvedora_id = desenvolvedora_id

            session.commit()

            return redirect(url_for('jogos.listar_jogos'))

        desenvolvedoras = session.scalars(select(Desenvolvedora)).all()

        return render_template("jogos/formulario.html", jogo=jogo,
                               desenvolvedoras=desenvolvedoras, titulo="Editar jogo",
                               acao=url_for('jogos.editar_jogo', id=id))

@jogos_bp.route('/jogos/<int:id>/excluir', methods=['POST', 'DELETE'])
def excluir_jogo(id):

    with Session() as session:
        jogo = session.get(Jogo, id)

        if jogo is None:
            abort(404)

        session.delete(jogo)
        session.commit()

    return redirect(url_for('jogos.listar_jogos'))

@jogos_bp.route('/jogos/<int:id>/clientes', methods=['GET'])
def listar_clientes_jogo(id):

    with Session() as session:
        jogo = session.get(Jogo, id)

        if jogo is None:
            abort(404)

        return render_template('jogos/clientes.html', jogo=jogo)
