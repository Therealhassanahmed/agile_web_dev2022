from app import app, db
from app.forms import RegistrationForm
from flask import render_template, flash, redirect, request, url_for
from app.forms import LoginForm
from app.models import Cities, User
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse



@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template("index.html", title='Home Page')

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


@app.route('/gaming')
def gaming():
    return render_template("gaming.html")

@app.route('/gamepage')
def gamepage():
    return render_template("gamepage.html")

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/countries', methods=['POST','GET'])
def countries():
    if request.method == "POST":
        friend_name = request.form['name']
        new_friend = Cities(cityname=friend_name)
        # Push to database
        db.session.add(new_friend)
        db.session.commit()
        return redirect('/countries')
    else:
        friends = Cities.query.order_by(Cities.id)
        return render_template("countries.html", friends=friends)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)