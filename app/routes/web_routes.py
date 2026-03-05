from fastapi import APIRouter, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.services.user_services import criar_usuario, logar_usuario

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

#==============================End-Points Home===========================
@router.get("/")
def home_page(request:Request):
    return templates.TemplateResponse("index.html", {"request":request})
#========================================================================


#===========================================End-Points Register==================================================
@router.get("/register")
def register_page(request:Request):
    return templates.TemplateResponse("register.html", {"request":request})

@router.post("/register")
def register_user(request:Request, username=Form(), email=Form(), password=Form(), db:Session = Depends(get_db)):
    criar_usuario(db, username, email, password)
    return RedirectResponse(url="/login", status_code=303)
#=================================================================================================================


#===========================================End-Points Login==================================
@router.get("/login")
def login_page(request:Request):
    return templates.TemplateResponse("login.html", {"request":request})

@router.post("/login")
def login_user(request:Request, email=Form(), password=Form(), db:Session = Depends(get_db)):
    if (logar_usuario(db, email, password)):
        return RedirectResponse(url="/", status_code=303)
    return templates.TemplateResponse("login.html", {"request":request})

#=============================================================================================


    