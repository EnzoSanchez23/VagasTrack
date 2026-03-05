from app.models.vagas import Vagas
from sqlalchemy.orm import Session

def criar_vaga(db:Session, nome_vaga:str, nome_empresa:str, local:str, salario:float, modelo_vaga:str, usuario_id:int, status_vaga:str="Em Progresso"):
    new_vaga = Vagas(nome_vaga=nome_vaga,
                     nome_empresa=nome_empresa,
                     local=local, salario=salario,
                     modelo_vaga=modelo_vaga,
                     status_vaga=status_vaga,
                     usuario_id=usuario_id
                     )
    
    db.add(new_vaga)
    db.commit()
    db.refresh(new_vaga)

    return new_vaga