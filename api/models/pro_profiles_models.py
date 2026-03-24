from pydantic import BaseModel, HttpUrl, Field
from models.models_configs import base_model_config
from typing import List, Optional
from datetime import datetime, date

class Image(BaseModel):
    model_config = base_model_config
    image_url: HttpUrl
    detail: str = Field(..., min_length=1)

class Experience(BaseModel):
    model_config = base_model_config
    start_date: date
    end_date: Optional[date] = None

class Certification(BaseModel):
    model_config = base_model_config
    name: str = Field(..., min_length=1)
    certificate_url: HttpUrl

class Address(BaseModel):
    model_config = base_model_config
    city: str = Field(..., min_length=1)
    address_detail: str = Field(..., min_length=1)

class ProProfile(BaseModel):
    model_config = base_model_config
    id: str | None = None
    provider_id: str | None = None
    profile_image: HttpUrl
    images: List[Image] = Field(..., max_length=5)
    name: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    experience: Experience
    certifications: List[Certification]
    addresses: List[Address] = Field(..., min_length=1)
    created_at: datetime | None = None
    updated_at: datetime | None = None
    is_active: bool = True
