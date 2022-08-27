from sqlalchemy.sql.expression import text
from sqlalchemy import Column, Integer, String, Boolean, BigInteger
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    seller_id = Column(Integer, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    category = Column(String, nullable=True)
    price = Column(BigInteger, nullable=False)
    description = Column(String, nullable=True)
    stock = Column(Integer, nullable=False)
    seller_id = Column(Integer, nullable=False)


class Contentmenu(Base):
    __tablename__ = "contentmenus"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=True)


class Media(Base):
    __tablename__ = "medias"
    id = Column(Integer, primary_key=True, nullable=False)
    media = Column(String, nullable=True)
    video = Column(String, nullable=True)
    menu_id = Column(Integer, nullable=True)
    product_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
