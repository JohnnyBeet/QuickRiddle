from sqlalchemy import Column, Integer, String, Sequence, CheckConstraint, ForeignKey


def create_word_riddles_tab(db):
    class WordRiddles(db.Model):
        __tablename__ = 'word_riddles'
        id = Column(Integer, Sequence("seq_word_riddles_id", start=1), primary_key=True, nullable=False)
        content = Column(String, nullable=False)
        answer = Column(String, nullable=False)
        level = Column(Integer,  ForeignKey("difficulty.id"), nullable=False)
        __table_args__ = (
            CheckConstraint('LENGTH(content) > 0'),
            CheckConstraint('LENGTH(answer) > 0'),
            CheckConstraint('level >= 1 AND level <= 3'),
        )
    return WordRiddles


def create_math_riddles_tab(db):
    class MathRiddles(db.Model):
        __tablename__ = 'math_riddles'
        id = Column(Integer, Sequence("seq_math_riddles_id", start=1), primary_key=True, nullable=False)
        content = Column(String, nullable=False)
        answer = Column(String, nullable=False)
        level = Column(Integer, ForeignKey("difficulty.id"), nullable=False)
        __table_args__ = (
            CheckConstraint('LENGTH(content) > 0'),
            CheckConstraint('LENGTH(answer) > 0'),
            CheckConstraint('level >= 1 AND level <= 3'),
        )
    return MathRiddles

