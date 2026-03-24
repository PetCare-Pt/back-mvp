from pydantic import BaseModel, HttpUrl, Field
from typing import Optional
from datetime import datetime, date
from models.models_configs import base_model_config

class PetProfile(BaseModel):
    model_config = base_model_config
    id: str | None = None
    owner_id: str | None = None
    name: str = Field(..., min_length=1)
    image_url: Optional[HttpUrl] = None
    species: str = Field(..., min_length=1)
    breed: Optional[str] = None
    birth_date: date
    weight: float = Field(..., gt=0)
    physical_description: Optional[str] = Field(default=None, min_length=1)
    special_notes: Optional[str] = Field(default=None, min_length=1)
    created_at: datetime | None = None
    updated_at: datetime | None = None
    is_active: bool = True