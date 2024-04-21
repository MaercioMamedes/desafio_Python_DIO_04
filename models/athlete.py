from datetime import datetime, date
from sqlalchemy import DateTime, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base_model import BaseModel


class AthleteModel(BaseModel):
    __tablename__ = "athletes"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    date_birth: Mapped[date] = mapped_column(Date, nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=False)
    height: Mapped[float] = mapped_column(Float, nullable=False)
    sex: Mapped[str] = mapped_column(String(1), nullable=False) # Mudar para Enum
    categorory: Mapped["CategoryModel"] = relationship(back_populates="Athlete", lazy="selectin")
    categorory_id: Mapped[int] = mapped_column(ForeignKey("categories.pk_id"))
    trainning_center: Mapped["TrainningCenterModel"] = relationship(back_populates="Athlete", lazy="selectin")
    trainning_center_id: Mapped[int] = mapped_column(ForeignKey("trainning_centers.pk_id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

