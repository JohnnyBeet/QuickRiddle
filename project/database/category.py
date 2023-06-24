from sqlalchemy import Column, Integer, String, Sequence


def create_category_tab(db):
    class Category(db.Model):
        __tablename__ = 'category'
        id = Column(Integer, Sequence("seq_category_id", start=1), primary_key=True)
        category = Column(String, nullable=False)
    return Category
