from pydantic import BaseModel, ConfigDict, HttpUrl, Field
from typing import List, Optional
from datetime import datetime

base_model_config = ConfigDict(
    populate_by_name=True,
    arbitrary_types_allowed=True,
    from_attributes=True,
)

class Image(BaseModel):
    model_config = base_model_config
    image_url: HttpUrl
    detail: str = Field(..., min_length=1)

class Experience(BaseModel):
    model_config = base_model_config
    start_date: datetime
    end_date: Optional[datetime] = None

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

class Response(BaseModel):
    message: str

def model_to_db(model: BaseModel) -> dict:
    data = model.model_dump(exclude_none=True, mode="json")
    if "id" in data:
        del data["id"]
    return data

def model_from_db(model_class: type[BaseModel], data: dict) -> BaseModel:
    if "_id" in data:
        data["id"] = str(data["_id"])
        del data["_id"]
    return model_class(**data)
