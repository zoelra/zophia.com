from flask.ext.sqlalchemy import SQLAlchemy
import os

from flask import Flask, render_template, request, session, flash, redirect, url_for, g
from functools import wraps
from hashlib import sha256

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Post


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))

    return wrap


@app.route('/', methods=["GET"])
def landing_page():
    posts = Post.query.all()
    print(posts)
    return render_template('visitor.html', posts=posts)


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


@app.route('/main')
def main():
    posts = Post.query.all()
    return render_template('visitor.html', posts=posts)


@app.route('/backend')
@login_required
def backend():
    posts = Post.query.all()
    return render_template('adding_posts.html', posts=posts)


@app.route('/add', methods=['POST'])
@login_required
def add():
    title = request.form['title']
    post = request.form['post']
    if not title or not post:
        flash("All fields are required. Please try again")
        return redirect(url_for('backend'))
    else:
        new_post = Post(
            title=title,
            post=post
        )
        db.session.add(new_post)
        db.session.commit()
        flash('New entry was successfully posted!')
        return redirect(url_for('backend'))


@app.route('/delete/<string:title>/')
@login_required
def delete_entry(title):
    post = Post.query.filter_by(title=title).first()
    db.session.delete(post)
    db.session.commit()
    flash('The post was deleted.')
    return redirect(url_for('backend'))


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
