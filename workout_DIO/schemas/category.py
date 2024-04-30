from typing import Annotated

from pydantic import UUID4, Field
from workout_DIO.schemas.BaseShema import BaseSchema


class CategoryInput(BaseSchema):
    name: Annotated[
        str,
        Field(description="Nome da categoria", example="Scale", max_length=10),
    ]


class CategoryOutput(CategoryInput):
    id: Annotated[UUID4, Field(description="Identificador da categoria")]
    name: Annotated[str, Field(description="Nome da categoria")]


class CategoryAthlete(BaseSchema):
    id: Annotated[UUID4, Field(description="id da categoria")]
