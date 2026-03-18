from fastapi import APIRouter, HTTPException, status
from database.mongo_db import db_dependency
from models.models import ProProfile, Response
from services.pro_profiles_service import create_profile, update_profile

pp_router = APIRouter(
    prefix="/pro_profiles",
    tags=["Professional profiles"],
    responses={404: {"description": "No se ha encontrado el recurso"}},
)

@pp_router.post("/")
async def create_pro_profile(db: db_dependency, pro_profile: ProProfile) -> Response:
    # TODO: Obtener provider_id y setearlo
    res, msg = create_profile(pro_profile, db["professional_profiles"])
    if not res:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg)
    return Response(message=msg)

@pp_router.put("/{pro_profile_id}")
async def update_pro_profile(db: db_dependency, pro_profile_id: str, pro_profile: ProProfile) -> Response:
    # TODO: Obtener provider_id y setearlo
    pro_profile.id = pro_profile_id
    res, msg = update_profile(pro_profile, db["professional_profiles"])
    if not res:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg)
    return Response(message=msg)