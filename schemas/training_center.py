from typing import Annotated

from pydantic import Field, UUID4
from .BaseShema import BaseSchema


class TranningCenterInput(BaseSchema):
    name: Annotated[str, Field(description="Nome do centro de Treinamento", example="CT King", max_length=20)]
    address: Annotated[str, Field(description="Endereço do centro de treinamento", example='Rua X, Q02', max_length=100)]
    owner: Annotated[str, Field(description="Proprietário do centro de treinamento", example="Marcos", max_length=30)]


class TranningCenterOutput(TranningCenterInput):
    id: Annotated[UUID4, Field(description='Identificador do centro de treinamento')]


class TrainningCenterAthlete(BaseSchema):
    name: Annotated[str, Field(description="Nome do centro de Treinamento", example="CT King", max_length=20)]
