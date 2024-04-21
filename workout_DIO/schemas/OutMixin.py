from datetime import datetime
from typing import Annotated

from pydantic import UUID4, Field

from .BaseShema import BaseSchema


class OutMixin(BaseSchema):
    id: Annotated[UUID4, Field(description="Identificador")]
    created_at: Annotated[datetime, Field(description="Data de criação")]
