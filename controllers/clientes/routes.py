from flask import Blueprint, render_template, request, redirect, url_for, abort
from sqlalchemy import select
from database import Session
from models.models import Cliente, Jogo
from werkzeug.security import generate_password_hash

clientes_bp = Blueprint('clientes', __name__, url_prefix='/clientes')


@clientes_bp.get('/')
def listar():
    with Session() as session:
        clientes = session.scalars(select(Cliente)).all()

    return render_template('clientes/listar.html', clientes=clientes)


@clientes_bp.route('/novo', methods =['GET', 'POST'])
def novo():
    if request.method == 'POST':
        nome = request.form['nome'].strip()
        email = request.form['email'].strip()
        senha = request.form['senha']

        if not nome or not email or not senha.strip():
            abort(400)

        cliente = Cliente(nome = nome, email = email, senha_hash = generate_password_hash(senha))

        with Session() as session:
            if session.scalars(select(Cliente).where(Cliente.email == email)).first():
                abort(400)

            session.add(cliente)
            session.commit()

        return redirect(url_for('clientes.listar'))

    return render_template('clientes/cadastro.html', titulo ='Novo cliente', cliente = None, acao = url_for('clientes.novo'))

@clientes_bp.get('/<int:id>')
def perfil(id):
    with Session() as session:
        cliente = session.get(Cliente, id)

        if cliente is None:
            return 'Cliente não encontrado', 404

        return render_template('clientes/perfil.html', cliente = cliente)

@clientes_bp.get('/<int:id>/biblioteca')
def biblioteca(id):
    with Session() as session:
        cliente = session.get(Cliente, id)


        if cliente is None:
            return 'Cliente não encontrado', 404

        jogos = session.scalars(select(Jogo)).all()
        disponiveis = [jogo for jogo in jogos if jogo not in cliente.jogos]
    
        return render_template('clientes/biblioteca.html', cliente = cliente, disponiveis=disponiveis)

@clientes_bp.post('/<int:id>/adicionar')
def adicionar(id):
    with Session() as session:
        cliente = session.get(Cliente, id)

        if cliente is None:
            return 'Cliente não encontrado', 404

        jogo_id = request.form.get('jogo_id', type=int)

        if jogo_id is None:
            abort(400)

        jogo = session.get(Jogo, jogo_id)

        if jogo is None:
            abort(404)

        if jogo not in cliente.jogos:
            cliente.jogos.append(jogo)
            session.commit()

    return redirect(url_for('clientes.biblioteca', id=id))

@clientes_bp.post('/<int:id>/remover/<int:jogo_id>')
def remover(id, jogo_id):
    with Session() as session:
        cliente = session.get(Cliente, id)
        jogo = session.get(Jogo, jogo_id)

        if cliente is None or jogo is None:
            return 'Cliente ou jogo não encontrado', 404

        if jogo in cliente.jogos:
            cliente.jogos.remove(jogo)
            session.commit()

    return redirect(url_for('clientes.biblioteca', id=id))
                

@clientes_bp.route('/editar/<int:id>', methods =['GET', 'POST'])
def editar(id):
    with Session() as session:
        cliente = session.get(Cliente, id)

        if cliente is None:
            return 'Cliente não encontrado', 404

        if request.method == 'POST':
            nome = request.form['nome'].strip()
            email = request.form['email'].strip()
            senha = request.form ['senha']

            if not nome or not email:
                abort(400)

            existente = session.scalars(select(Cliente).where(Cliente.email == email)).first()

            if existente and existente.id != cliente.id:
                abort(400)

            cliente.nome = nome
            cliente.email = email
            if senha:
                cliente.senha_hash = generate_password_hash(senha)

            session.commit()

            return redirect(url_for('clientes.listar'))
    
        return render_template('clientes/cadastro.html', titulo = 'Editar cliente', cliente = cliente,acao=url_for('clientes.editar', id=id))

@clientes_bp.post('/excluir/<int:id>')
def excluir(id):
    with Session() as session:
        cliente = session.get(Cliente, id)

        if cliente is None:
            return 'Cliente não encontrado', 404

        session.delete(cliente)
        session.commit()

    return redirect(url_for('clientes.listar'))        

            