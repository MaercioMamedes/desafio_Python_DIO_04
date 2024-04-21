from typing import Annotated
from pydantic import UUID4, BaseModel, Field
from datetime import datetime

from .BaseShema import BaseSchema


class OutMixin(BaseSchema):
    id: Annotated[UUID4, Field(description='Identificador')]
    created_at: Annotated[datetime, Field(description='Data de criação')]
