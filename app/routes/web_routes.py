from fastapi import APIRouter, Request, Depends, Form, Cookie
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.services.user_services import criar_usuario, logar_usuario, deletar_usuario
from app.services.vagas_services import criar_vaga, editar_vaga_selecionada, deletar_vaga_selecionada
from app.models.user import User
from app.models.vagas import Vagas
from app.core.sessions import get_user_id, criar_session, delete_session

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


#============================Funções Auxiliares================================
def get_current_user(session_id:str = Cookie(None), db:Session = Depends(get_db)):
    if not session_id:
        return None

    user_id = get_user_id(session_id)

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
        session_id = criar_session(user.id)

        if (user.id == 1):
            response = RedirectResponse(url="/admin", status_code=303)
            response.set_cookie(
                key="session_id",
                value=session_id,
                httponly=True,
                samesite="lax"
                )
            return response
        
        response = RedirectResponse(url="/", status_code=303)
        response.set_cookie(
            key="session_id",
            value=session_id,
            httponly=True,
            samesite="lax"
            )
        return response
     
    return templates.TemplateResponse("login.html", {"request":request})

#=============================================================================================



#===========================================End-Points Vagas==================================
@router.post("/nova-vaga")
def criar_nova_vaga(request:Request, vaga=Form(), empresa=Form(), local=Form(), salario=Form(), modelo=Form(), user=Depends(get_current_user),db:Session=Depends(get_db)):
    vaga = criar_vaga(db,vaga,empresa,local,salario,modelo,usuario_id=user.id)
    if(vaga):
        response = RedirectResponse(url="/", status_code=303)
        return response


@router.post("/editar-vaga")
def editar_vaga(request:Request, id=Form() ,vaga=Form(), empresa=Form(), local=Form(), salario=Form(), modelo=Form(), status=Form(), db:Session=Depends(get_db)):
    vaga_editada = editar_vaga_selecionada(db, id, vaga, empresa, local, salario, modelo, status)
    if(vaga_editada):
        response = RedirectResponse(url="/", status_code=303) 
        return response


@router.post("/deletar-vaga")
def deletar_vaga(request:Request, db:Session=Depends(get_db), idVaga=Form(), user=Depends(get_current_user)):
    
    vaga = deletar_vaga_selecionada(db, idVaga, user.id)

    if (vaga):
        return RedirectResponse(url="/", status_code=303)

#================================================================================================



#===========================================End-Points Logout===================================
@router.get("/logout")
def logout_user(request:Request, session_id:str=Cookie(None)):
    if(session_id):
        delete_session(session_id)
    
    response = RedirectResponse(url="/login", status_code=303)
    response.delete_cookie(key="session_id")
    return response
#================================================================================================



#===========================================End-Points Admin===================================
@router.get("/admin")
def admin_page(request:Request, user=Depends(get_current_user), db:Session=Depends(get_db)):

    vagas = db.query(Vagas).all()
    usuarios = db.query(User).filter(User.id != 1).all()

    if not user:
        response = RedirectResponse(url="/login", status_code=303)
        return response

    if(user.id != 1):
        response = RedirectResponse(url="/", status_code=303)
        return response
    
    return templates.TemplateResponse(
        "admin.html",{"request":request, "user": user, "vagas":vagas, "usuarios": usuarios})


@router.post("/admin-delete-user")
def admin_delete_user(request:Request, db:Session=Depends(get_db), idUsuario=Form()):
    usuario_selecionado = deletar_usuario(db, idUsuario)

    if(usuario_selecionado):

        return RedirectResponse(url="/admin", status_code=303)

#================================================================================================

