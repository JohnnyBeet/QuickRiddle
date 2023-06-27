from project import app
from project.database.create_database import create_tables


if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
