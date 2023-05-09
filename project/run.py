from flask import Flask, render_template, url_for, request, jsonify
import json
app = Flask(__name__)

difficulty = ''
type = ''

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


@app.route("/difficulty")
def difficulty():
    return render_template('difficulty.html')

@app.route("/riddle")
def riddle():
    return render_template('riddle.html')

@app.route("/type_post", methods=['POST'])
def type_post():
    type = json.loads(request.get_json())['type']
    app.logger.info(f"Chosen type: {type}")
    return type

@app.route("/difficulty_post", methods=['POST'])
def difficulty_post():
    difficulty = json.loads(request.get_json())['difficulty']
    app.logger.info(f"Chosen difficulty: {difficulty}")
    return difficulty


if __name__ == '__main__':
    app.run(debug=True)