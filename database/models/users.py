from sqlalchemy import Column, Integer, String, Sequence, CheckConstraint
from sqlalchemy.types import ARRAY



class Users:
    __tablename__ = 'users'
    id = Column(Integer, Sequence("seq_users_id", start=0), primary_key=True)
    user_name = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    math_riddles = Column(ARRAY(Integer), nullable=True, default=[])
    word_riddles = Column(ARRAY(Integer), nullable=True, default=[])
    __table_args__ = (
        CheckConstraint("LENGTH(user_name) > 0")
    )
