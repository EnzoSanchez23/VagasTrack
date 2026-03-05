from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.database.database import Base, engine
from app.routes.web_routes import router
from app.models.user import User
from app.models.vagas import Vagas

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Servir arquivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(router)

