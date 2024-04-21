from typing import Annotated, Optional
from datetime import date
from pydantic import Field, PositiveFloat

from .category import CategoryInput
from .training_center import TrainningCenterAthlete
from .BaseShema import BaseSchema
from .OutMixin import OutMixin


class Athlete(BaseSchema):
    name: Annotated[str, Field(description='Nome do atleta', example='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', example='12345678900', max_length=11)]
    date_birth: Annotated[date, Field(description='data de nacimento do atleta', example="25/02/1998")]  # Verificar entrada, saída e validação de dados
    weight: Annotated[PositiveFloat, Field(description='Peso do atleta', example=75.5)]
    height: Annotated[PositiveFloat, Field(description='Altura do atleta', example=1.70)]
    sex: Annotated[str, Field(description='Sexo do atleta', example='M', max_length=1)]
    category: Annotated[CategoriaIn, Field(description='Categoria do atleta')]
    trainning_center: Annotated[TrainningCenterAthlete, Field(description='Centro de treinamento do atleta')]


class AthleteInput(Athlete):
    pass


class AthleteOutPut(Athlete, OutMixin):
    pass


class AthleteUpdate(BaseSchema):
    name: Annotated[Optional[str], Field(None, description='Nome do atleta', example="João", max_length=50)]
    date_birth: Annotated[Optional[date], Field(None, description='data de nascimento do atleta', example="24/02/25")]
