from project import app, db
from project.database.create_database import create_tables


if __name__ == '__main__':
    create_tables(db)
    app.run(debug=True)
