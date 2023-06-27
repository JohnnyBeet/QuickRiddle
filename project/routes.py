from flask import render_template, url_for, request, flash, redirect
from project.forms import SingupForm, LoginForm
from project import app
from project.src.random_riddle import random_riddle
from project.src.save_riddle import save_riddle
from project.src.user_administration import insert_user, check_user_credentials, load_user
from project.src.stats import get_number_of_riddles, get_number_of_correct_riddles
from flask_login import login_user, current_user, logout_user

category = None
difficulty = None


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = check_user_credentials(form.login.data, form.password.data)
        if user:
            login_user(user)
            return redirect(url_for("home"))
        else:
            flash('Login unsuccessfull. Please check username and password.', 'danger')
    return render_template('login.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = SingupForm()
    if form.validate_on_submit():
        insert_user(form.login.data, form.password.data)
        flash(f"Your account has been created!. You can now log in.", 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)


@app.route("/difficulty", methods=['GET', 'POST'])
def difficulty():
    if current_user.is_authenticated:
        if request.method == 'POST':
            global category
            category = request.form.get('cat_value')
            app.logger.info(f"Chosen category: {str(category)}")
        return render_template('difficulty.html')
    return redirect(url_for('login'))


@app.route("/riddle", methods=['GET', 'POST'])
def riddle():
    if current_user.is_authenticated:
        if request.method == 'POST':
            global difficulty
            difficulty = request.form.get('diff_value')
            app.logger.info(f"Chosen difficulty: {str(difficulty)}")

        global random_quiz
        random_quiz = random_riddle(category=category, difficulty=difficulty)
        app.logger.info(f"Chosen riddle ID: {str(random_quiz.id)}")
        return render_template('riddle.html', quiz_content=random_quiz.content)
    return redirect(url_for('login'))


@app.route('/assessment', methods=['GET', 'POST'])
def assessment():
    if current_user.is_authenticated:
        user_answer = request.form.get("user_answer")
        correct_answer = random_quiz.answer
        callback = 'Error'
        if user_answer.lower() == correct_answer.lower():
            callback = 'Correct'
            save_riddle(random_quiz, True)
        else:
            callback = 'Incorrect'
            save_riddle(random_quiz, False)
        return render_template('assessment.html', callback=callback, right_answer=correct_answer)


@app.route("/stats", methods=['GET', 'POST'])
def stats():
    if current_user.is_authenticated:
        user = load_user(current_user.get_id())

        number_of_completed_riddles = get_number_of_riddles()
        number_of_math_riddles = get_number_of_riddles('math_riddle')
        number_of_word_riddles = get_number_of_riddles('word_riddle')

        number_of_correct_riddles = get_number_of_correct_riddles()
        number_of_correct_math_riddles = get_number_of_correct_riddles('math_riddle')
        number_of_correct_word_riddles = get_number_of_correct_riddles('word_riddle')

        percent_of_correct_riddles = round(number_of_correct_riddles/number_of_completed_riddles, ndigits=2)
        percent_of_correct_math_riddles = round(number_of_correct_math_riddles/number_of_math_riddles, ndigits=2)
        percent_of_correct_word_riddles = round(number_of_correct_word_riddles/number_of_word_riddles, ndigits=2)


        return render_template('stats.html', user=user)
    return redirect(url_for('login'))
