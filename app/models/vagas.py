from sqlalchemy import Column, Integer, String, ForeignKey, Float
from app.database.database import Base, SessionLocal
from sqlalchemy.orm import relationship

class Vagas(Base):

    __tablename__ = "vagas"

    id = Column("ID", Integer, primary_key=True, autoincrement=True)
    nome_vaga = Column("nome_vaga", String)
    nome_empresa = Column("nome_empresa", String)
    local = Column("local", String)
    salario = Column("salario", Float)
    modelo_vaga = Column("modelo_vaga", String)
    status_vaga = Column("status_vaga", String)
    usuario_id = Column("usuario_id", Integer, ForeignKey("users.ID"))
    usuario = relationship("User", back_populates="vagas")