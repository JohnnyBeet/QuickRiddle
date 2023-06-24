from flask import render_template, url_for, request
import json
from project import app
from project.src.random_riddle import random_riddle

category = None
difficulty = None


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/signup")
def signup():
    return render_template('signup.html')


@app.route("/difficulty",methods=['GET','POST'])
def difficulty():
    if request.method == 'POST':
        global category
        category = request.form.get('cat_value')
        app.logger.info(f"Chosen category: {str(category)}")
    return render_template('difficulty.html')


@app.route("/riddle",methods=['GET','POST'])
def riddle():
    if request.method == 'POST':
        if 'diff_value' in request.form:
            global difficulty
            difficulty = request.form.get('diff_value')
            app.logger.info(f"Chosen difficulty: {str(difficulty)}")
        elif 'user_answer' in request.form:
            print(request.form.get('user_answer'))

    random_quiz = random_riddle(category=category, difficulty=difficulty)
    return render_template('riddle.html',quiz_content=random_quiz.content)
