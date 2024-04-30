from typing import Dict, Any
from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy.future import select
from datetime import datetime
from pprint import pprint
from copy import copy

from workout_DIO.config.database import DatabaseDependency
from workout_DIO.schemas.athlete import AthleteInput, AthleteUpdate, AthleteOutPutFinal, AthleteOutPut
from workout_DIO.models.trainning_center import TrainningCenterModel
from workout_DIO.models.athlete import AthleteModel
from workout_DIO.models.category import CategoryModel
from workout_DIO.models.base_model import BaseModel

router = APIRouter()


@router.post(
    path="/",
    summary="criar novo atleta",
    status_code=status.HTTP_201_CREATED,
    response_model=AthleteOutPut
)
async def post(
        db_session: DatabaseDependency,
        athlete_in: AthleteInput = Body(...),
) -> AthleteOutPut:

    def model_dict_formater(obj: BaseModel) -> dict:
        obj_dict = obj.__dict__
        obj_dict.__delitem__("_sa_instance_state")
        obj_dict.__delitem__("pk_id")
        return obj_dict

    category: CategoryModel = (
        await db_session.execute(select(CategoryModel).filter_by(id=athlete_in.category.id))
    ).scalars().first()

    if not category:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID da Categoria inválida"
        )
    trainning_center: TrainningCenterModel = (
        await db_session.execute(select(TrainningCenterModel).filter_by(id=athlete_in.trainning_center.id))
    ).scalars().first()

    if not trainning_center:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID daCentro de Treinamento inválido"
        )

    category_dict = model_dict_formater(copy(category))
    trainning_center_dict = model_dict_formater(copy(trainning_center))

    athlete_dict = athlete_in.model_dump()
    athlete_dict['category'] = category_dict
    athlete_dict['trainning_center'] = trainning_center_dict

    athlete: AthleteOutPut = AthleteOutPut(id=uuid4(), created_at=datetime.utcnow(), **athlete_dict)

    athlete_model = AthleteModel(**athlete.model_dump(exclude={"category", "trainning_center"}))

    athlete_model.categorory_id = category.pk_id
    athlete_model.trainning_center_id = trainning_center.pk_id
    db_session.add(athlete_model)

    pprint(athlete_model.__dict__)
    await db_session.commit()

    return athlete


@router.get(
    path="/{id_athlete}",
    summary="Buscar Atleta pelo ID",
    status_code=status.HTTP_200_OK,
    response_model=AthleteOutPut
)
async def get(
        id_athlete: UUID4,
        db_sesssion: DatabaseDependency
) -> AthleteOutPutFinal:
    athlete: AthleteOutPutFinal = (
        await db_sesssion.execute(select(AthleteModel).filter_by(id=id_athlete))
    ).scalars().first()

    return athlete


@router.get(
    path="/",
    summary="Buscar todos os atletas cadastrados",
    status_code=status.HTTP_200_OK,
    response_model=list[AthleteOutPut]
)
async def query(
        db_session: DatabaseDependency
) -> list[AthleteOutPut]:

    athlete_list: list[AthleteOutPut] = (
        await db_session.execute(select(AthleteModel))
    ).scalars().all()

    return athlete_list

