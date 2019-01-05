from flask import render_template
from app import myapp


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
