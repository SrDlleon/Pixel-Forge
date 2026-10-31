from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from sqlalchemy import select
from database import Session
from models.models import Desenvolvedora

desenvolvedora_bp = Blueprint('desenvolvedoras', __name__, url_prefix='/desenvolvedoras')


@desenvolvedora_bp.get('/')
def listar():
    with Session() as session:
        desenvolvedoras = session.scalars(select(Desenvolvedora)).all()
        return render_template('desenvolvedoras/listar.html', desenvolvedoras=desenvolvedoras)


@desenvolvedora_bp.get('/<int:id>')
def detalhes(id):
    with Session() as session:
        desenvolvedora = session.get(Desenvolvedora, id)

        if desenvolvedora is None:
            abort(404)

        return render_template('desenvolvedoras/detalhes.html', desenvolvedora=desenvolvedora)



@desenvolvedora_bp.route('/nova', methods=['GET', 'POST'])
def nova():
    if request.method == 'POST':
        nome = request.form['nome'].strip()

        if not nome:
            flash('Nome é obrigatório')
        else:
            with Session() as session:
                desenvolvedora = Desenvolvedora(nome=nome)
                session.add(desenvolvedora)
                session.commit()

            return redirect(url_for('desenvolvedoras.listar'))

    return render_template('desenvolvedoras/formulario.html',
                           titulo='Cadastrar desenvolvedora',
                           desenvolvedora=None,
                           acao=url_for('desenvolvedoras.nova'))


@desenvolvedora_bp.route('/<int:id>/editar', methods=['GET', 'POST'])
def editar(id):
    with Session() as session:
        desenvolvedora = session.get(Desenvolvedora, id)

        if desenvolvedora is None:
            abort(404)

        if request.method == 'POST':
            nome = request.form['nome'].strip()

            if not nome:
                flash('Nome é obrigatório')
            else:
                desenvolvedora.nome = nome
                session.commit()
                return redirect(url_for('desenvolvedoras.listar'))

        return render_template('desenvolvedoras/formulario.html',
                               titulo='Editar desenvolvedora',
                               desenvolvedora=desenvolvedora,
                               acao=url_for('desenvolvedoras.editar', id=id))


@desenvolvedora_bp.post('/<int:id>/excluir')
def excluir(id):
    with Session() as session:
        desenvolvedora = session.get(Desenvolvedora, id)

        if desenvolvedora is None:
            abort(404)

        if desenvolvedora.jogos:
            flash('Exclua os jogos desta desenvolvedora primeiro.')
            return redirect(url_for('desenvolvedoras.listar'))

        session.delete(desenvolvedora)
        session.commit()

    return redirect(url_for('desenvolvedoras.listar'))
