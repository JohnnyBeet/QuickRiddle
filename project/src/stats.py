from project import db
from project.database.create_database import CompletedRiddles, Riddles, Category
from flask_login import current_user


def get_number_of_riddles(category='all'):
    if category != 'all':
        completed_riddles = db.session.query(CompletedRiddles).join(Riddles).join(Category).filter(
            CompletedRiddles.user_id == current_user.get_id(),
            Category.category == category
        )
    else:
        completed_riddles = db.session.query(CompletedRiddles).filter(CompletedRiddles.user_id == current_user.get_id())
    return completed_riddles.count()


def get_number_of_correct_riddles(category='all'):
    if category != 'all':
        completed_riddles = db.session.query(CompletedRiddles).join(Riddles).join(Category).filter(
            CompletedRiddles.user_id == current_user.get_id(),
            CompletedRiddles.correct_answer == True,
            Category.category == category
        )
    else:
        completed_riddles = db.session.query(CompletedRiddles).filter(
            CompletedRiddles.user_id == current_user.get_id(),
            CompletedRiddles.correct_answer == True)
    return completed_riddles.count()


