from pymongo.database import Collection
from models.pro_profiles_models import ProProfile
from models.mappers import model_to_db
from datetime import datetime
from bson.objectid import ObjectId

def create_profile(pro_profile: ProProfile, db: Collection) -> dict[str | None, str]:
    now = datetime.now()
    is_valid, msg = verify_pro_profile_experience(pro_profile, now)
    if not is_valid:
        return None, msg
    if db.count_documents({"provider_id": pro_profile.provider_id}) > 0:
        return None, "Ya has creado tu perfil profesional"
    pro_profile.updated_at = now
    pro_profile.created_at = now
    pro_profile.is_active = True
    result = db.insert_one(model_to_db(pro_profile))
    return str(result.inserted_id), "Perfil profesional creado exitosamente"

def update_profile(pro_profile: ProProfile, db: Collection) -> dict[str | None, str]:
    now = datetime.now()
    is_valid, msg = verify_pro_profile_experience(pro_profile, now)
    if not is_valid:
        return None, msg
    if db.count_documents({"provider_id": pro_profile.provider_id, 
                           "_id": ObjectId(pro_profile.id)}) == 0:
        return None, "No tienes un perfil profesional creado"
    p_id, prov_id = pro_profile.id, pro_profile.provider_id
    pro_profile.updated_at = now
    data_dict = model_to_db(pro_profile)
    del data_dict["provider_id"]
    del data_dict["created_at"]
    del data_dict["is_active"]
    result = db.update_one({"provider_id": prov_id, "_id": ObjectId(p_id)}, {"$set": data_dict})
    return str(result.modified_count), "Perfil profesional actualizado exitosamente"

def verify_pro_profile_experience(pro_profile: ProProfile, now: datetime) -> dict[bool, str | None]:
    if pro_profile.experience:
        if pro_profile.experience.start_date > now.date():
            return False, "La fecha de inicio de la experiencia no puede ser posterior a la fecha actual"
        if pro_profile.experience.end_date \
            and pro_profile.experience.end_date < pro_profile.experience.start_date:
            return False, "La fecha de finalización de la experiencia no puede ser anterior a la fecha de inicio"
    return True, None