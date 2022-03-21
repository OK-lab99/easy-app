from fastapi import APIRouter
from routers import token, user, article

api_router = APIRouter()

api_router.include_router(token.router)
api_router.include_router(user.router)
api_router.include_router(article.router)