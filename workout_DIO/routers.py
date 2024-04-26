from fastapi import APIRouter
from workout_DIO.controllers.category_controller import router as category
from workout_DIO.controllers.trainning_center_controller import router as trainning_center


api_router = APIRouter()
api_router.include_router(category, prefix='/category', tags=['categorias'])
api_router.include_router(trainning_center, prefix="/trainning-center", tags=["Centro de Treinamento"])
