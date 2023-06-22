from sqlalchemy import Column, Integer, String, Sequence, CheckConstraint, ForeignKey


def create_riddles_tab(db):
    class Riddles(db.Model):
        __tablename__ = 'riddles'
        id = Column(Integer, Sequence('seq_riddles_id', start=1), primary_key=True)
        content = Column(String, nullable=False)
        answer = Column(String, nullable=False)
        level = Column(Integer,  ForeignKey("difficulty.id"), nullable=False)
        category = Column(Integer, ForeignKey("category.id"))
        __table_args__ = (
            CheckConstraint('LENGTH(content) > 0'),
            CheckConstraint('LENGTH(answer) > 0'),
        )
    return Riddles




