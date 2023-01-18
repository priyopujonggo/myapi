from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, oauth2
from ..database import get_db

router = APIRouter(prefix="/api/products", tags=["Products"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.Product])
def get_products(menu_id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    products = db.query(models.Product).all()
    return products


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Products)
def create_products(product: schemas.ProductCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_product = models.Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product
