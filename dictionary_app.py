from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# words = list()
# words = ['парта', 'выдра', 'уголь', 'рыжик', 'пирог', 'рукав', 'порка', 'спина', 'длань']  # DEV


app = FastAPI()


@app.get("/word/{word_id}", response_model=schemas.Word)
def get_word(word_id: int, db: Session = Depends(get_db)):
    word = crud.get_word(db, word_id).word
    return {"word": word}


@app.get("/words_count")
def get_words_count(db: Session = Depends(get_db)):
    count = crud.get_words_count(db)
    return {"words_count": count}


@app.post("/add_word/", response_model=schemas.Word)
def add_word(word: schemas.WordCreate, db: Session = Depends(get_db)):
    return crud.create_word(db, word)
