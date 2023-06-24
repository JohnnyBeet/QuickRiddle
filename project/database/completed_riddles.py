from sqlalchemy import Column, Integer, Sequence, Boolean, ForeignKey


def create_completed_riddles_tab(db):
    class CompletedRiddles(db.Model):
        __tablename__ = 'completed_riddles'
        id = Column(Integer, Sequence("seq_completed_riddles_id", start=1), primary_key=True)
        user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
        riddle_id = Column(Integer, ForeignKey("riddles.id"), nullable=False)
        correct_answer = Column(Boolean, nullable=False)

    return CompletedRiddles
