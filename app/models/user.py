from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.database import Base, SessionLocal


class User(Base):

    __tablename__ = "users"

    id = Column("ID", Integer, primary_key=True, autoincrement=True, index=True)
    nome_usuario = Column("nome_usuario", String)
    email = Column("email", String, unique=True)
    senha = Column("password", String)
    vagas = relationship("Vagas", back_populates="usuario")