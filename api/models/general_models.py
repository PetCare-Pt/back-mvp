from pydantic import BaseModel

class CreationResponse(BaseModel):
    message: str
    data_id: str