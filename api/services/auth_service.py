from firebase_admin import auth
from fastapi import Depends, HTTPException, status
from typing import Annotated
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

def get_current_user_id(credentials: HTTPAuthorizationCredentials = Depends(security)) -> str:
    token = credentials.credentials
    try:
        user_info = auth.verify_id_token(token)
        return user_info.get("uid", "")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado"
        )

user_id_dependency = Annotated[str, Depends(get_current_user_id)]
