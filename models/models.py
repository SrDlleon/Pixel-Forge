from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


# Tabela intermediária para o relacionamento N:N
cliente_jogo = Table(
    "cliente_jogo",
    Base.metadata,
    Column("cliente_id", Integer, ForeignKey("clientes.id"), primary_key=True),
    Column("jogo_id", Integer, ForeignKey("jogos.id"), primary_key=True)
)


class Desenvolvedora(Base):
    __tablename__ = "desenvolvedora"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(255), nullable=False)

    # Relacionamento 1:N
    jogos: Mapped[list["Jogo"]] = relationship(back_populates="desenvolvedora")


class Cliente(Base):
    __tablename__ = "clientes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    senha_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    # Relacionamento N:N
    jogos: Mapped[list["Jogo"]] = relationship(
        secondary=cliente_jogo,
        back_populates="clientes"
    )


class Jogo(Base):
    __tablename__ = "jogos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    titulo: Mapped[str] = mapped_column(String(255), nullable=False)

    # Chave estrangeira 1:N
    desenvolvedora_id: Mapped[int] = mapped_column(ForeignKey("desenvolvedora.id"), nullable=False)

    # Relacionamento com Desenvolvedora
    desenvolvedora: Mapped["Desenvolvedora"] = relationship(back_populates="jogos")

    # Relacionamento N:N com Cliente
    clientes: Mapped[list["Cliente"]] = relationship(secondary=cliente_jogo, back_populates="jogos")
