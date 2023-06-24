from project.database.create_database import Riddles, Difficulty, Category
from project import db
from sqlalchemy.sql.expression import func

def random_riddle(category:str, difficulty:str):
    matching_diff_cat = db.session.query(Riddles).join(Difficulty).join(Category).filter(
        Difficulty.level == difficulty,
        Category.category == category
    )
    
    result = matching_diff_cat.order_by(func.random()).first()

    return result