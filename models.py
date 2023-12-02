from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Text
from database import meta, engine

categories_model = Table(
    "categories",
    meta,
    Column('id', Integer, primary_key=True),
    Column('name',
           String(100), nullable=False),
    Column('slug', String(100), nullable=False)
)

products_model = Table(
    "products",
    meta,
    Column('id', Integer, primary_key=True),
    Column('name',
           String(100), nullable=False),
    Column('slug', String(100), nullable=False),
    Column('description', String(100), nullable=False),
    Column('price', Integer, default=0),
    Column('categories_id', Integer, ForeignKey('categories.id')),
)

products_photos_model = Table(
    "product_photos",
    meta,
    Column('id', Integer, primary_key=True),
    Column('name',
           String(100), nullable=False),
    Column('products_id', Integer, ForeignKey('products.id')),
)

meta.create_all(engine)