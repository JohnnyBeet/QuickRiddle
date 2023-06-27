from project.database.create_database import CompletedRiddles
from project import db
from flask_login import current_user


def save_riddle(riddle_output, isCorrect):
    new_row = CompletedRiddles(riddle_id=riddle_output.id, user_id=current_user.get_id(), correct_answer=isCorrect)
    db.session.add(new_row)
    db.session.commit()
