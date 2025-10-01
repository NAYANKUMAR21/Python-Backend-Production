from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "healthy"}

@router.get("/health/db")
async def health_check_db(db: Session = Depends(get_db)):
    try:
        db.execute("SELECT 1")
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": str(e)}
