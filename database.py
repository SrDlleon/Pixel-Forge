from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

engine = create_engine("sqlite:///pixel_forge.db")

Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(
    model_class=Base
)