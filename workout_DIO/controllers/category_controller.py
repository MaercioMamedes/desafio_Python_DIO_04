from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from workout_DIO.schemas.category import CategoryInput, CategoryOutput
from workout_DIO.models.category import CategoryModel

from workout_DIO.config.database import DatabaseDependency
from sqlalchemy.future import select

router = APIRouter()


@router.post(
    "/",
    summary="Criar nova Categoria",
    status_code=status.HTTP_201_CREATED,
    response_model=CategoryOutput,

)
async def post(
        db_session: DatabaseDependency,
        category_in: CategoryInput = Body(...)
) -> CategoryOutput:
    categoria_out = CategoryOutput(id=uuid4(), **category_in.model_dump())
    categoria_model = CategoryModel(**categoria_out.model_dump())

    db_session.add(categoria_model)
    await db_session.commit()
    return categoria_out
