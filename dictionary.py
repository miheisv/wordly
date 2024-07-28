from random import choice
from fastapi import FastAPI


words = list()
words = ['парта', 'выдра', 'уголь', 'рыжик', 'пирог', 'рукав', 'порка', 'спина', 'длань']  # DEV

app = FastAPI()


@app.get("/random_word")
def get_word():
    return {"word": choice(words)}
