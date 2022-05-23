from distutils.util import execute
from multiprocessing import synchronize
from os import stat
from typing import Any, Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel

from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user, auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


while True:

    try:
        conn = psycopg2.connect(host='localhost', database='myapi',
                                user='postgres', password='root', cursor_factory=RealDictCursor)

        cursor = conn.cursor()
        print("Database connection was successfully")
        break
    except Exception as error:
        print("Database connection was failed")
        print(error)
        time.sleep(2)


my_posts = [{"title": "title of post 1", "content": "content of First post", "id": 1}, {
    "title": "favorite foods", "content": "I like Pizza", "id": 2}]


def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "Priyo Pujonggo"}
