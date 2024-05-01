from datetime import date
from typing import Annotated, Optional

from pydantic import Field, PositiveFloat, UUID4

from .BaseShema import BaseSchema
from .category import CategoryAthlete, CategoryOutput
from .OutMixin import OutMixin
from .training_center import (TrainningCenterAthleteInput,
                              TranningCenterOutput,
                              TrainningCenterOutPutList)


class Athlete(BaseSchema):
    name: Annotated[
        str, Field(description="Nome do atleta", example="Joao", max_length=50)
    ]
    cpf: Annotated[
        str,
        Field(
            description="CPF do atleta", example="12345678900", max_length=11
        ),
    ]
    date_birth: Annotated[
        date,
        Field(description="data de nacimento do atleta", example="1991-05-23"),
    ]  # Verificar entrada, saída e validação de dados
    weight: Annotated[
        PositiveFloat, Field(description="Peso do atleta", example=75.5)
    ]
    height: Annotated[
        PositiveFloat, Field(description="Altura do atleta", example=1.70)
    ]
    sex: Annotated[
        str, Field(description="Sexo do atleta", example="M", max_length=1)
    ]
    category: Annotated[
        CategoryAthlete, Field(description="ID da categoria do Atleta")
    ]
    trainning_center: Annotated[
        TrainningCenterAthleteInput,
        Field(description="Centro de treinamento do atleta"),
    ]


class AthleteInput(Athlete):
    pass


class AthleteOutputList(BaseSchema):
    id: Annotated[
        UUID4, Field(description="Identificador")
    ]
    name: Annotated[
        str, Field(description="Nome do atleta", example="Joao", max_length=50)
    ]
    category: Annotated[
        CategoryOutput, Field(description="categoria")
    ]

    trainning_center: Annotated[
        TrainningCenterOutPutList, Field(description="Centro de Treinamento")
    ]


class AthleteOutPut(OutMixin):
    name: Annotated[
        str, Field(description="Nome do atleta", example="Joao", max_length=50)
    ]
    cpf: Annotated[
        str,
        Field(
            description="CPF do atleta", example="12345678900", max_length=11
        ),
    ]
    date_birth: Annotated[
        date,
        Field(description="data de nacimento do atleta", example="1991-05-23"),
    ]  # Verificar entrada, saída e validação de dados
    weight: Annotated[
        PositiveFloat, Field(description="Peso do atleta", example=75.5)
    ]
    height: Annotated[
        PositiveFloat, Field(description="Altura do atleta", example=1.70)
    ]
    sex: Annotated[
        str, Field(description="Sexo do atleta", example="M", max_length=1)
    ]

    category: Annotated[
        CategoryOutput, Field(description="categoria")
    ]

    trainning_center: Annotated[
        TranningCenterOutput, Field(description="Centro de Treinamento")
    ]


class AthleteUpdate(BaseSchema):
    weight: Annotated[
        Optional[PositiveFloat], Field(None)
    ]
    category: Annotated[
        Optional[CategoryAthlete], Field(None)
    ]
    trainning_center: Annotated[
        Optional[TrainningCenterAthleteInput],
        Field(None),
    ]
