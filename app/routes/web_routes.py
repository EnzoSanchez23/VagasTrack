from fastapi import APIRouter, Request, Depends, Form, Cookie
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.services.user_services import criar_usuario, logar_usuario
from app.services.vagas_services import criar_vaga
from app.models.user import User
from app.models.vagas import Vagas

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


#============================Funções Auxiliares================================
def get_current_user(user_id:str = Cookie(None), db:Session = Depends(get_db)):
    if not user_id:
        return None

    return db.query(User).filter_by(id=int(user_id)).first()
#==============================================================================



#==============================End-Points Home===========================
@router.get("/")
def home_page(request:Request, user=Depends(get_current_user), db:Session=Depends(get_db)):

    if not user:
        return RedirectResponse("/login", status_code=303)

    vagas = db.query(Vagas).filter_by(usuario_id=user.id).all()

    return templates.TemplateResponse(
        "index.html",
        {
            "request":request,
            "user": user,
            "vagas": vagas 
        })
#========================================================================




#===========================================End-Points Register==================================================
@router.get("/register")
def register_page(request:Request):
    return templates.TemplateResponse("register.html", {"request":request})

@router.post("/register")
def register_user(request:Request, username=Form(), email=Form(), password=Form(), db:Session = Depends(get_db)):
    if criar_usuario(db, username, email, password):
        return RedirectResponse(url="/login", status_code=303)
    return templates.TemplateResponse("register.html", {"request":request})
#=================================================================================================================




#===========================================End-Points Login==================================
@router.get("/login")
def login_page(request:Request):
    return templates.TemplateResponse("login.html", {"request":request})

@router.post("/login")
def login_user(request:Request, email=Form(), password=Form(), db:Session = Depends(get_db)):
    user = logar_usuario(db, email, password)
    if (user):
        response = RedirectResponse(url="/", status_code=303)
        response.set_cookie(
            key="user_id",
            value=str(user.id),
            httponly=True
            )
        
        return response
     
    return templates.TemplateResponse("login.html", {"request":request})

#=============================================================================================




#===========================================End-Points Adicionar Vaga==================================
@router.post("/nova-vaga")
def criar_nova_vaga(request:Request, vaga=Form(), empresa=Form(), local=Form(), salario=Form(), modelo=Form(), user=Depends(get_current_user),db:Session=Depends(get_db)):
    vaga = criar_vaga(db,vaga,empresa,local,salario,modelo,usuario_id=user.id)
    if(vaga):
        response = RedirectResponse(url="/", status_code=303)
        return response
#======================================================================================================