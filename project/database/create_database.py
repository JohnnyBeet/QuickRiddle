import pandas as pd

from .difficulty_level import create_difficulty_tab
from .riddles import create_math_riddles_tab, create_word_riddles_tab
from .users import create_users_table

from project import app


def insert_difficulty_level(db, Difficulty):
    low = Difficulty(level='low')
    medium = Difficulty(level='medium')
    high = Difficulty(level='high')
    db.session.add(low)
    db.session.add(medium)
    db.session.add(high)
    db.session.commit()


def insert_math_riddles(db):
    math_data = pd.read_csv("database/zadania_kangur.csv", sep=";")
    math_data["Question"] = math_data["Question"] + ' ' + math_data["A"] + ' ' + math_data["B"] + ' ' + math_data[
        "C"] + ' ' + math_data["D"] + ' ' + math_data["E"]
    math_data = math_data.drop(columns=["A", "B", "C", "D", "E"])
    math_data.rename(columns={"Question": "content", "Answer": "answer", "Level": "level"}, inplace=True)
    math_data.index += 1
    math_data.index.names = ['id']
    math_data.to_sql("math_riddles", con=db.engine, if_exists="append")


def insert_word_riddles(db):
    word_data = pd.read_csv("database/word_riddles.csv", sep=";")
    word_data.rename(columns={"QUESTIONS": "content", "ANSWERS": "answer", "Difficulty": "level"}, inplace=True)
    word_data.index += 1
    word_data.index.names = ['id']
    word_data.to_sql("word_riddles", con=db.engine, if_exists="append")


def create_tables(db):
    Difficulty = create_difficulty_tab(db)
    MathRiddles = create_math_riddles_tab(db)
    WordRiddles = create_word_riddles_tab(db)
    Users = create_users_table(db)
    with app.app_context():
        db.create_all()
        if db.session.query(Difficulty).first() is None:
            insert_difficulty_level(db, Difficulty)
        if db.session.query(MathRiddles).first() is None:
            insert_math_riddles(db)
        if db.session.query(WordRiddles).first() is None:
            insert_word_riddles(db)