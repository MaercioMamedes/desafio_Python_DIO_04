from typing import Annotated

from pydantic import UUID4, Field
from workout_api.contrib.schemas import BaseSchema


class CategoryInput(BaseSchema):
    nome: Annotated[
        str,
        Field(description="Nome da categoria", example="Scale", max_length=10),
    ]


class CategoryOutput(CategoryInput):
    id: Annotated[UUID4, Field(description="Identificador da categoria")]