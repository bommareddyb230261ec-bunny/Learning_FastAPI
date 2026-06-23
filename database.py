from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url="postgresql://postgres:Charan.56@localhost:5432/fastapi_crud_db"
engine=create_engine(db_url)
session=sessionmaker(autocommit=False,autoflush=False,bind=engine)
