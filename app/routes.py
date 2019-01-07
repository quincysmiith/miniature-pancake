from flask import render_template, flash, redirect
from app import myapp
from app.forms import LoginForm


@myapp.route('/')
@myapp.route('/index')
def index():
    user = {'username': 'Marquin'}

    posts = [
        {
            'author': {'username': 'Marquin'},
            'body': 'Its stormy in sydney'
        },

        {
            'author': {'username': 'Caroline'},
            'body': 'I like cheese'
        }

    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@myapp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
