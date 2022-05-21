from app import app, db
from app.forms import RegistrationForm
from flask import render_template, flash, redirect, request, url_for
from app.forms import LoginForm
from app.models import User, Location
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse



@app.route('/')
@app.route('/index')
@login_required
def index():
    form = LoginForm()
    user_leaderboard_easy = User.query.order_by(User.high_score_easy.desc())[0:4]
    user_leaderboard_normal = User.query.order_by(User.high_score_normal.desc())[0:4]
    user_leaderboard_hard = User.query.order_by(User.high_score_hard.desc())[0:4]
    return render_template("index.html", title='Home Page', form=form, user_leaderboard_easy=user_leaderboard_easy, user_leaderboard_normal=user_leaderboard_normal, user_leaderboard_hard=user_leaderboard_hard)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/hard', methods=['GET', 'POST'])
def hard():
    location = Location.query.all()
    form = request.form
    highscore = 0
    if request.method == 'POST':
        highscore = form["postit"]
        currentuser = User.query.get(current_user.id)
        if currentuser.high_score_hard >= int(highscore):
            None
        else:
            currentuser.high_score_hard = int(highscore)
            db.session.commit()
    return render_template("hard.html", location=location, cities=cities, countries=countries, populations=populations, highscore=highscore)

@app.route('/normal', methods=['GET', 'POST'])
def normal():
    location = Location.query.all()
    form = request.form
    highscore = 0
    if request.method == 'POST':
        highscore = form["postit"]
        currentuser = User.query.get(current_user.id)
        if currentuser.high_score_normal >= int(highscore):
            None
        else:
            currentuser.high_score_normal = int(highscore)
            db.session.commit()
    return render_template("normal.html", location=location, cities=cities, countries=countries, populations=populations, highscore=highscore)

@app.route('/easy', methods=['GET', 'POST'])
def easy():
    location = Location.query.all()
    form = request.form
    highscore = 0
    if request.method == 'POST':
        highscore = form["postit"]
        currentuser = User.query.get(current_user.id)
        if currentuser.high_score_easy >= int(highscore):
            None
        else:
            currentuser.high_score_easy = int(highscore)
            db.session.commit()
    return render_template("easy.html", location=location, cities=cities, countries=countries, populations=populations, highscore=highscore)

def cities():
    lst = []
    location = Location.query.all()
    for x in range(len(location)):
        lst.append(location[x].City)
    return lst
def countries():
    lst = []
    location = Location.query.all()
    for x in range(len(location)):
        lst.append(location[x].Country)
    return lst
def populations():
    lst = []
    location = Location.query.all()
    for x in range(len(location)):
        lst.append(location[x].Population)
    return lst

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, high_score_easy=0, high_score_normal=0, high_score_hard=0)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)