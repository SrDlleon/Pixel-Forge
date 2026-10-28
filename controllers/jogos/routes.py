from flask import Blueprint
from flask import methods

jogos_bp = Blueprint('jogos', __name__)

@jogos_bp.route('/jogos', methods=['GET'])
def listar_jogos():
    return "lista de jogos"

@jogos_bp.route('/jogos/<int:id>', methods=['GET'])
def detalhar_jogo():
    return "detalhar jogo"

@jogos_bp.route('/jogos/novo', methods=['POST'])
def novo_jogo():
    return "novo jogo"

@jogos_bp.route('/jogos/<int:id>/editar', methods=['PUT'])
def editar_jogo():
    return "editar jogo"

@jogos_bp.route('/jogos/<int:id>/excluir', methods=['DELETE'])
def excluir_jogo():
    return "excluir jogo"