from pydantic import BaseModel


class WordBase(BaseModel):
    word: str
    lenght: int


class WordCreate(WordBase):
    pass


class Word(WordBase):
    id: int

    class Config:
        from_attributes = True
