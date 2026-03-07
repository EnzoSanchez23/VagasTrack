from app.models.user import User
from sqlalchemy.orm import Session

def criar_usuario(db:Session, nome_usuario:str, email:str, senha:str):
    print(f"nome_usuario: {nome_usuario} | email: {email} | senha: {senha}")
    new_user = User(nome_usuario=nome_usuario, email=email, senha=senha)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    #return new_user

def logar_usuario(db:Session, email:str, senha:str):
    current_user = db.query(User).filter_by(email=email, senha=senha).first()
    if current_user:
        print(f"email: {email} | senha: {senha}")
        print("Usuario logado!")
        return current_user
    print("Usuario Invalido!")
    return None