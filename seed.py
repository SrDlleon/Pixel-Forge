
from database import Base, engine, Session
from models.models import Desenvolvedora, Cliente, Jogo

Base.metadata.create_all(engine)

with Session() as session:

    valve = Desenvolvedora(nome="Valve")

    portal = Jogo(
        titulo="Portal 2",
        desenvolvedora=valve
    )

    cliente = Cliente(
        nome="João",
        email="joao@email.com",
        senha_hash="hash_de_exemplo"
    )

    cliente.jogos.append(portal)

    session.add_all([valve, portal, cliente])
    session.commit()

print("Banco de dados populado com sucesso!")
