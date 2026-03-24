from pydantic import BaseModel

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
