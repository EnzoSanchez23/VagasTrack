from app.models.vagas import Vagas
from sqlalchemy.orm import Session

def criar_vaga(db:Session, nome_vaga:str, nome_empresa:str, local:str, salario:float, modelo_vaga:str, usuario_id:int, status_vaga:str="Em Processo"):
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

def editar_vaga_selecionada(db:Session, id:int, nome_vaga:str, nome_empresa:str, local:str, salario:float, modelo_vaga:str, status_vaga:str):
    vaga_atual = db.query(Vagas).filter_by(id=id).first()
    
    if not vaga_atual:
        return None
    
    vaga_atual.nome_vaga = nome_vaga
    vaga_atual.nome_empresa = nome_empresa
    vaga_atual.local = local
    vaga_atual.salario = salario
    vaga_atual.modelo_vaga = modelo_vaga
    vaga_atual.status_vaga = status_vaga

    db.commit()
    db.refresh(vaga_atual)

    return vaga_atual

def deletar_vaga_selecionada(db:Session, vaga_id:int, user_id:int):
    deletar_vaga_selecionada = db.query(Vagas).filter_by(id=vaga_id, usuario_id=user_id).first()

    if not deletar_vaga_selecionada:
        return None

    db.delete(deletar_vaga_selecionada)
    db.commit()
    return deletar_vaga_selecionada