from sqlalchemy import Column, Integer, String, Sequence


def create_difficulty_tab(db):
    class Difficulty(db.Model):
        __tablename__ = 'difficulty'
        id = Column(Integer, Sequence("seq_difficulty_id", start=1), primary_key=True)
        level = Column(String, nullable=False)
    return Difficulty

