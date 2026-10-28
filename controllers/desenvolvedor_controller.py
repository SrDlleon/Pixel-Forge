from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from sqlalchemy import select
from database import Session
from models import Desenvolvedora

desenvolvedora_bp = Blueprint('desenvolvedoras', __name__, url_prefix='/desenvolvedoras')


@desenvolvedora_bp.get('/desenvolvedoras/listar')
def listar():
    




#/desenvolvedoras > listar desenvolvedoras
#/desenvolvedoras/nova > cadastrar dev
#/desenvolvedoras/<id> >> visualizar dados da dev
#/desenvolvedoras/<id>/editar >> editar desenvolvedora
#/desenvolvedoras/<id>/excluir >> excluir dev
#/desenvolvedoras/<id>/jogos >> listar jogos publicados pela dev