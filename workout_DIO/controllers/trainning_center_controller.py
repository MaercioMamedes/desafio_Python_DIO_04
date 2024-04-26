from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException, status
from pydantic import UUID4
from sqlalchemy.future import select

from workout_DIO.config.database import DatabaseDependency
from workout_DIO.models.trainning_center import TrainningCenterModel
from workout_DIO.schemas.training_center import (TrainningCenterAthlete,
                                                 TranningCenterInput,
                                                 TranningCenterOutput,
                                                 TrainningCenterPartialUpdate)

router = APIRouter()


@router.post(
    path="/",
    summary="Criar Centro de Treinamento",
    status_code=status.HTTP_201_CREATED,
    response_model=TranningCenterOutput,
)
async def post(
        db_session: DatabaseDependency,
        trainning_center_in: TranningCenterInput = Body(...)
) -> TranningCenterOutput:
    trainning_center = TranningCenterOutput(id=uuid4(), **trainning_center_in.model_dump())
    trainning_center_model = TrainningCenterModel(**trainning_center.model_dump())

    db_session.add(trainning_center_model)
    await db_session.commit()
    return trainning_center


@router.get(
    path="/",
    summary="Buscar centros de treinamento",
    status_code=status.HTTP_200_OK,
    response_model=list[TranningCenterOutput]
)
async def query(db_session: DatabaseDependency) -> list[TranningCenterOutput]:
    trainning_centers: list[TranningCenterOutput] = (
        await db_session.execute(select(TrainningCenterModel))
    ).scalars().all()

    return trainning_centers


@router.get(
    path="/{id_ct}",
    summary="Buscar Centro de Treinamento pelo id",
    status_code=status.HTTP_200_OK,
    response_model=TranningCenterOutput
)
async def get(
        id_ct: UUID4,
        db_session: DatabaseDependency
) -> TranningCenterOutput:
    trainnig_center: TranningCenterOutput = (
        await db_session.execute(select(TrainningCenterModel).filter_by(id=id_ct))
    ).scalars().first()

    if not trainnig_center:
        raise HTTPException(
            detail="Centro de treinamento não encontrado",
            status_code=status.HTTP_404_NOT_FOUND
        )

    else:
        return trainnig_center

@router.patch(
    path="/{id_ct}",
    summary="Atualizar Centro de Treinamento Parciamente",
    status_code=status.HTTP_200_OK,
)
async def patch(
        id_ct,
        db_session: DatabaseDependency,
        trainning_center_in: TrainningCenterPartialUpdate = Body(...),
):
    trainnig_center: TranningCenterOutput = (
        await db_session.execute(select(TrainningCenterModel).filter_by(id=id_ct))
    ).scalars().first()

    if not trainnig_center:
        raise HTTPException(
            detail="Centro de treinamento não encontrado",
            status_code=status.HTTP_404_NOT_FOUND
        )

    else:
        ct_update = trainning_center_in.model_dump(exclude_unset=True)
        for key, value in ct_update.items():
            setattr(trainnig_center, key, value)

        await db_session.commit()
        await db_session.refresh(trainnig_center)

        return trainnig_center


@router.delete(
    path="/{id_ct}",
    summary="Deletar Centro de treinamento a partir do id",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete(
        id_ct: UUID4,
        db_session: DatabaseDependency
):
    trainnig_center: TranningCenterOutput = (
        await db_session.execute(select(TrainningCenterModel).filter_by(id=id_ct))
    ).scalars().first()

    if not trainnig_center:
        raise HTTPException(
            detail="Centro de treinamento não encontrado",
            status_code=status.HTTP_404_NOT_FOUND
        )

    else:

        await db_session.delete(trainnig_center)
        await db_session.commit()
