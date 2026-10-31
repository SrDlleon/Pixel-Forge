from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import select
from database import Session
from models.models import Cliente
from werkzeug.security import generate_password_hash

clientes_bp = Blueprint('clientes', __name__, url_prefix ='/clientes')

@clientes_bp.get('/')
def listar():
    with Session() as session:
        clientes = session.scalars(select(Cliente)).all()

        return render_template('clientes/listar.html', clientes = clientes)

@clientes_bp.route('inicio', methods = ['GET', 'POST'])
def inicio():
    if request.method == 'POST':
        nome = request.form ['nome']
        email = request.form ['email']
        senha = request.form ['senha']

        cliente = Cliente (nome = nome, email = email, senha_hash = generate_password_hash(senha))

        with Session() as session:
            session.add(cliente)
            session.commit()

        return redirect(url_for('cliente.listar'))

    return render_template ('clientes/cadastro.html', titulo = 'inicio cliente', cliente = none, acao = url_for('clientes.inicio'))