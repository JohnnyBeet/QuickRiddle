from flask import render_template, url_for, request, flash, redirect
from project.forms import SingupForm, LoginForm
import json
from project import app
from project.src.random_riddle import random_riddle
from project.src.save_riddle import save_riddle

category = None
difficulty = None


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route("/signup",methods=['GET','POST'])
def signup():
    form = SingupForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.login.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('signup.html', form=form)


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
        global difficulty
        difficulty = request.form.get('diff_value')
        app.logger.info(f"Chosen difficulty: {str(difficulty)}")

    global random_quiz
    random_quiz = random_riddle(category=category, difficulty=difficulty)
    app.logger.info(f"Chosen riddle ID: {str(random_quiz.id)}")
    return render_template('riddle.html',quiz_content=random_quiz.content)

@app.route('/assessment',methods=['GET','POST'])
def assessment():
    user_answer = request.form.get("user_answer")
    correct_answer = random_quiz.answer
    callback = 'Error'
    if user_answer.lower() == correct_answer.lower():
        callback = 'Correct'
        save_riddle(random_quiz,True)
    else:
        callback = 'Incorrect'
        save_riddle(random_quiz,False)
    return render_template('assessment.html',callback=callback,right_answer=correct_answer)