from fastapi import APIRouter, HTTPException, status
from database.mongo_db import db_dependency
from models.pets_profiles_models import PetProfile
from models.general_models import CreationResponse
from services.pets_profiles_service import create_profile, update_profile
from services.auth_service import user_id_dependency

pep_router = APIRouter(
    prefix="/pets_profiles",
    tags=["Pets profiles"],
    responses={404: {"description": "No se ha encontrado el recurso"}},
)

@pep_router.post("/")
async def create_pet_profile(db: db_dependency, owner_id: user_id_dependency, 
                             pet_profile: PetProfile) -> CreationResponse:
    pet_profile.owner_id = owner_id
    res, msg = create_profile(pet_profile, db["pets"])
    if not res:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg)
    return CreationResponse(message=msg, data_id=res)

@pep_router.put("/{pet_profile_id}")
async def update_pet_profile(db: db_dependency, owner_id: user_id_dependency, 
                             pet_profile_id: str, pet_profile: PetProfile) -> CreationResponse:
    pet_profile.owner_id = owner_id
    pet_profile.id = pet_profile_id
    res, msg = update_profile(pet_profile, db["pets"])
    if not res:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg)
    return CreationResponse(message=msg, data_id=res)