from pymongo.database import Collection
from models.pets_profiles_models import PetProfile
from models.mappers import model_to_db
from datetime import datetime
from bson.objectid import ObjectId

def create_profile(pet_profile: PetProfile, db: Collection) -> dict[str | None, str]:
    now = datetime.now()
    is_valid, msg = verify_birthdate(pet_profile, now)
    if not is_valid:
        return None, msg
    pet_profile.updated_at = now
    pet_profile.created_at = now
    pet_profile.is_active = True
    result = db.insert_one(model_to_db(pet_profile))
    return str(result.inserted_id), "Perfil de mascota creado exitosamente"

def update_profile(pet_profile: PetProfile, db: Collection) -> dict[str | None, str]:
    now = datetime.now()
    is_valid, msg = verify_birthdate(pet_profile, now)
    if not is_valid:
        return None, msg
    prof_id, owner_id = pet_profile.id, pet_profile.owner_id
    pet_profile.updated_at = now
    data_dict = model_to_db(pet_profile)
    del data_dict["owner_id"]
    del data_dict["created_at"]
    del data_dict["is_active"]
    result = db.update_one({"owner_id": owner_id, "_id": ObjectId(prof_id)}, {"$set": data_dict})
    return str(result.modified_count), "Perfil de mascota actualizado exitosamente"

def verify_birthdate(pet_profile: PetProfile, now: datetime) -> dict[bool, str | None]:
    if pet_profile.birth_date > now.date():
        return False, "La fecha de nacimiento no puede ser posterior a la fecha actual"
    return True, None