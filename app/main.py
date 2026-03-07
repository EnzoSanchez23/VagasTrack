from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.database.database import Base, engine, SessionLocal
from app.routes.web_routes import router
from app.models.user import User
from dotenv import load_dotenv
import os

app = FastAPI()
load_dotenv()

Base.metadata.create_all(bind=engine)

db = SessionLocal()
admin_user = os.getenv("ADMIN_USER")
admin_email = os.getenv("ADMIN_EMAIL")
admin_password = os.getenv("ADMIN_PASSWORD")

admin = db.query(User).filter_by(nome_usuario=admin_user,email=admin_email).first()
if not admin:
    admin = User(nome_usuario=admin_user, email=admin_email, senha=admin_password)
    db.add(admin)
    db.commit()

# Servir arquivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(router)