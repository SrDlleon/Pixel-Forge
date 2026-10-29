from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from sqlalchemy import select
from database import Session
from models.models import Desenvolvedora

desenvolvedora_bp = Blueprint('desenvolvedoras', __name__, url_prefix='/desenvolvedoras')


@desenvolvedora_bp.get('/desenvolvedoras/listar')
def listar():
    with Session() as session:
        desenvolvedora = session.scalars(select(Jogo)).all()

        return render_template("desenvolvedoras/listar.html", desenvolvedora=desenvolvedora)
    




#/desenvolvedoras > listar desenvolvedoras
#/desenvolvedoras/nova > cadastrar dev
#/desenvolvedoras/<id> >> visualizar dados da dev
#/desenvolvedoras/<id>/editar >> editar desenvolvedora
#/desenvolvedoras/<id>/excluir >> excluir dev
#/desenvolvedoras/<id>/jogos >> listar jogos publicados pela dev