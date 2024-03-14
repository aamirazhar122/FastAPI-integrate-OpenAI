from sqlmodel import SQLModel, Session, Field, select
from typing import Optional
from sqlalchemy import create_engine  
from dotenv import load_dotenv, find_dotenv
from os import getenv

_ : bool = load_dotenv(find_dotenv())

class prompt(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    text: str

postgres_url = getenv("POSTGRESS_URL", "")
engine = create_engine(postgres_url, echo=True)

def create_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__" :
    create_tables()
