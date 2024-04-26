from fastapi import APIRouter
from workout_DIO.controllers.category_controller import router as category


api_router = APIRouter()
api_router.include_router(category, prefix='/category', tags=['categorias'])
