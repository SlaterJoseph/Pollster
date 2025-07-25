from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/poll", tags=["poll"])