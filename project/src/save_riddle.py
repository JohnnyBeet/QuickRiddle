from project.database.create_database import Riddles, Difficulty, Category, Users, CompletedRiddles
from project import db

def save_riddle(riddle_output, isCorrect):
    new_row = CompletedRiddles(riddle_id = riddle_output.id, user_id = 1, correct_answer = isCorrect)
    db.session.add(new_row)
    db.session.commit()