from sqlalchemy import Column, Integer, String, Sequence, CheckConstraint


class WordRiddles:
    __tablename__ = 'word_riddles'
    id = Column(Integer, Sequence("seq_word_riddles_id", start=0), primary_key=True, nullable=False)
    content = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    level = Column(Integer, nullable=False)
    __table_args__ = (
        CheckConstraint('LENGTH(content) > 0'),
        CheckConstraint('LENGTH(answer) > 0'),
        CheckConstraint('level >= 1 AND level <= 3'),
    )


class MathRiddles:
    __tablename__ = 'math_riddles'
    id = Column(Integer, Sequence("seq_math_riddles_id", start=0), primary_key=True, nullable=False)
    content = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    level = Column(Integer, nullable=False)
    __table_args__ = (
        CheckConstraint('LENGTH(content) > 0'),
        CheckConstraint('LENGTH(answer) > 0'),
        CheckConstraint('level >= 1 AND level <= 3'),
    )

