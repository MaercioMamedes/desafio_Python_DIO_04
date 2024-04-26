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
async def post(  # cadastrar nova categoria
        db_session: DatabaseDependency,
        category_in: CategoryInput = Body(...)
) -> CategoryOutput:
    categoria_out = CategoryOutput(id=uuid4(), **category_in.model_dump())
    categoria_model = CategoryModel(**categoria_out.model_dump())

    db_session.add(categoria_model)
    await db_session.commit()
    return categoria_out


@router.get(
    path="/",
    summary="Consultar todas as Categorias cadastradas",
    status_code=status.HTTP_200_OK,
    response_model=list[CategoryOutput]
)
async def query(db_session: DatabaseDependency) -> list[CategoryOutput]:
    categories: list[CategoryOutput] = (await db_session.execute(select(CategoryModel))).scalars().all()

    return categories


@router.get(
    "/{id_category}",
    summary="Consulta uma categoria pelo id",
    status_code=status.HTTP_200_OK,
    response_model=CategoryOutput
)
async def get(id_category: UUID4, db_session: DatabaseDependency) -> CategoryOutput:
    category: CategoryOutput = (
        await db_session.execute(select(CategoryModel).filter_by(id=id_category))
    ).scalars().first()

    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category not found in id {id_category}"
        )

    return category


@router.delete(
    path="/{id_category}",
    summary="Deletar uma categoria pelo id",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete(id_category: UUID4, db_session: DatabaseDependency):
    category: CategoryOutput = (
        await db_session.execute(select(CategoryModel).filter_by(id=id_category))
    ).scalars().first()

    if not category:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category not found in id {id_category}"
        )

    else:
        await db_session.delete(category)
        await db_session.commit()

@router.put(
    path="/{id_category}",
    summary="Atualizar nome da Categoria",
    status_code=status.HTTP_200_OK,
)
async def put(
        id_category: UUID4,
        db_session: DatabaseDependency,
        category_in: CategoryInput = Body(...)
        ) -> CategoryOutput:

    category: CategoryOutput = (
        await db_session.execute(select(CategoryModel).filter_by(id=id_category))
    ).scalars().first()

    if not category:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category not found in id {id_category}"
        )

    else:
        category.name = category_in.name

        db_session.add(category)
        await db_session.commit()
        return category
