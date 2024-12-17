from fastapi import APIRouter

from app.api.endpoints import key_value, pdf, password

router = APIRouter()
router.include_router(key_value.router, prefix="/key_value", tags=["key_value"])
router.include_router(pdf.router, prefix="/pdf", tags=["pdf"])
router.include_router(password.router, prefix="/password", tags=["password"])
