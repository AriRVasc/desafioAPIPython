from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt


SECRET_KEY = "Ari$"
ALGORITHM = "HS256"

router = APIRouter()
scurity=HTTPBearer

def criar_jwt_token(username: str) -> str:
    payload = {"username": username}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verificar_jwt_token(token: str = Depends(HTTPBearer())) -> str:
    try:
        credentials = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        username = credentials.get("username")
        if not username:
            raise HTTPException(status_code=401, detail="Token inválido")
        return username
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")


@router.post("/auth")
def autenticar(username: str, password: str):

    if username == "usuario" and password == "senha":
        token = criar_jwt_token(username)
        return {"access_token": token}
    else:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

