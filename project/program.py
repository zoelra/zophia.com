from flask import Flask, render_template, request, session, flash, redirect, url_for
from functools import wraps
from hashlib import sha256
from flask_sqlalchemy import SQLAlchemy
import os

DATABASE = 'zophia_blog.db'
USERNAME = 'fe7d80792aba17b08e301d3910bdef10e755086b2d03fa3ab99064a7ceff03cf'
PASSWORD = '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918'
SECRET_KEY = """b'|\xa9={5YR\x02{\x00\x97\xda\x16\x11L\x05\xbe\x1b\xde\xe9M\xbe\x8c\x89'"""

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))

    return wrap


# visitor view


@app.route('/', methods=["GET"])
def landing_page():

    posts = db.session.query(Post)
    flash('Welcome!')
    return render_template('visitor.html', posts=posts)


@app.route('/main/', methods=["GET"])
def main():
    posts = db.session.query(Post)
    flash('Welcome!')
    return render_template('visitor.html', posts=posts)


# admin view


@app.route('/admin', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if sha256(request.form['username'].encode('utf-8')).hexdigest() \
                != app.config['USERNAME'] \
                or sha256(request.form['password'].encode('utf-8')).hexdigest() \
                != app.config['PASSWORD']:
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('backend'))
    return render_template('login.html', error=error)


@app.route('/backend')
@login_required
def backend():
    posts = db.session.query(posts).order_by(posts.post_date.asc())
    return render_template('adding_posts.html', posts=posts)


@app.route('/add/', methods=['GET', 'POST'])
@login_required
def add():
    title = request.form['title']
    post = request.form['post']
    if not title or not post:
        flash("All fields are required. Please try again")
        return redirect(url_for('backend'))
    else:
        db.session.add(add)
        db.session.commit()
        flash('New entry was successfully posted!')
        return redirect(url_for('backend'))


@app.route('/delete/<string:title>/')
@login_required
def delete_entry(title):
    post_id = title
    db.session.query(title).filter_by(title=post_id).delete()
    db.session.commit()
    flash('The post was deleted.')
    return redirect(url_for('backend'))


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))
