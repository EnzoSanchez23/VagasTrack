from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.database.database import Base, engine
from app.routes.web_routes import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Servir arquivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(router)