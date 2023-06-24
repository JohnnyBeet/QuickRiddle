import pandas as pd

from .difficulty_level import create_difficulty_tab
from .riddles import create_riddles_tab
from .users import create_users_table
from .category import create_category_tab
from .completed_riddles import create_completed_riddles_tab

from project import app,db

Difficulty = create_difficulty_tab(db)
Category = create_category_tab(db)
Riddles = create_riddles_tab(db)
Users = create_users_table(db)
CompletedRiddles = create_completed_riddles_tab(db)

def insert_difficulty_level(db, Difficulty):
    low = Difficulty(level='low')
    medium = Difficulty(level='medium')
    high = Difficulty(level='high')
    db.session.add(low)
    db.session.add(medium)
    db.session.add(high)
    db.session.commit()


def insert_categories(db, Category):
    word_riddle = Category(category='word_riddle')
    math_riddle = Category(category='math_riddle')
    db.session.add(word_riddle)
    db.session.add(math_riddle)
    db.session.commit()


def insert_math_riddles(db, Riddles):
    math_data = pd.read_csv("project/database/zadania_kangur.csv", sep=";")
    math_data["Question"] = math_data["Question"] + ' ' + math_data["A"] + ' ' + math_data["B"] + ' ' + math_data[
        "C"] + ' ' + math_data["D"] + ' ' + math_data["E"]
    math_data = math_data.drop(columns=["A", "B", "C", "D", "E"])
    math_data.rename(columns={"Question": "content", "Answer": "answer", "Level": "level"}, inplace=True)
    math_data["category"] = 2
    # math_data.to_sql("riddles", con=db.engine, if_exists="append", index=False)
    for index, data in math_data.iterrows():
        row = Riddles(content=data["content"], answer=data['answer'], level=data['level'], category=data['category'])
        db.session.add(row)
    db.session.commit()


def insert_word_riddles(db, Riddles):
    word_data = pd.read_csv("project/database/word_riddles.csv", sep=";")
    word_data.rename(columns={"QUESTIONS": "content", "ANSWERS": "answer", "Difficulty": "level"}, inplace=True)
    word_data['category'] = 1
    # word_data.to_sql("riddles", con=db.engine, if_exists="append", index=False)
    for index, data in word_data.iterrows():
        row = Riddles(content=data["content"], answer=data['answer'], level=data['level'], category=data['category'])
        db.session.add(row)
    db.session.commit()


def create_tables(db):
    with app.app_context():
        db.create_all()
        if db.session.query(Difficulty).first() is None:
            insert_difficulty_level(db, Difficulty)
        if db.session.query(Category).first() is None:
            insert_categories(db, Category)
        if db.session.query(Riddles).first() is None:
            insert_math_riddles(db, Riddles)
            insert_word_riddles(db, Riddles)
