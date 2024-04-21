from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_model import BaseModel


class TrainningCenterModel(BaseModel):
    __tablename__ = "trainning_centers"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    address: Mapped[str] = mapped_column(String(100), nullable=False)
    owner: Mapped[str] = mapped_column(String(30), nullable=False)
    athlete: Mapped['AthleteModel'] = relationship(back_populates="trainning_center")
