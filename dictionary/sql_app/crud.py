from sqlalchemy.orm import Session

from . import models, schemas


def get_word(db: Session, word_id: int):
    return db.query(models.Word).filter(models.Word.id == word_id).one()


def create_word(db: Session, word: schemas.WordCreate):
    db_word = models.Word(word=word.word, lenght=word.lenght)
    db.add(db_word)
    db.commit()
    db.refresh(db_word)
    return db_word


def get_words_count(db: Session):
    return db.query(models.Word).count()
