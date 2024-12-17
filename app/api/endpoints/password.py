from fastapi import APIRouter, HTTPException
from app.services.password_service import generate_password, hash_password, check_password

router = APIRouter()


@router.get("/password/generate/")
def generate_new_password(length: int = 12):
    try:
        password = generate_password(length)
        return {"password": password}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/password/hash/")
def hash_user_password(password: str):
    try:
        hashed_password = hash_password(password)
        return {"hashed_password": hashed_password}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/password/check/")
def check_user_password(password: str, hashed_password: str):
    try:
        is_valid = check_password(password, hashed_password)
        return {"is_valid": is_valid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
