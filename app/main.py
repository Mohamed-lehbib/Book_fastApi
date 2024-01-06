from fastapi import FastAPI
from .model import Base
from .config import engine
from . import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

# @app.get('/')
# async def Home():
#     return "Welcome Home"

app.include_router(router=router.router, prefix="/book", tags=["book"])