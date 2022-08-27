from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, oauth2
from ..database import get_db

router = APIRouter(prefix="/api/products", tags=["Products"])


@router.get("/", response_model=List[schemas.Product])
def get_products(menu_id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    products = db.query(models.Product).join(
        models.Media).filter(models.Product.id == models.Media.menu_id)

    return products
