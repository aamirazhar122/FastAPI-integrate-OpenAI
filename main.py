from fastapi import FastAPI, HTTPException, status, Depends
from database import prompt, Session, engine, SQLModel, select
from typing import List, Optional, Annotated
from utils import user_answer

class Prompt(SQLModel):
    id : int | None
    text : str

class CreatePrompt(SQLModel):
    text : str


app : FastAPI = FastAPI()

def get_db():
    with Session(engine) as session:
        yield session

@app.get("/prompt", response_model=List[prompt])
def get_user(session : Annotated[Session, Depends(get_db)]):
    prmt = session.exec(select(prompt)).all()
    return prmt

@app.post("/prompt/post")
def post_prompt(pro : CreatePrompt, session : Annotated[Session, Depends(get_db)] ):
    pro_to_insert = prompt.model_validate(pro)
    session.add(pro_to_insert)
    session.commit()
    session.refresh(pro_to_insert)
    return pro_to_insert


@app.post("/prompt/")
def write_prompt(Prompt :CreatePrompt):
    Prompt_text = user_answer(f'Prompt text : {Prompt.text}')
    return Prompt_text
