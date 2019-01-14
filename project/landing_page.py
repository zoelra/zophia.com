from flask import Flask, render_template, request, session, flash, redirect, url_for, g
from functools import wraps
import sqlite3


DATABASE = 'zophia.db'
SECRET_KEY = '\xcf\xd6~w\xbb\x97\xb5\xa9f\x0f\xd1\x14@]-'

app = Flask(__name__)


app.config.from_object(__name__)



def connect_db():
	return sqlite3.connect(app.config['DATABASE'])


@app.route('/main')
def main():
	g.db = connect_db()
	cur = g.db.execute('select * from posts')
	posts = [dict(title=row[0], post=row[1]) for row in cur.fetchall()]
	g.db.close()
	return render_template('main.html', posts=posts)

# @app.route('/add', methods=['POST'])
# def add():
# 	title = request.form['title']
# 	post = request.form['post']
# 	if not title or not post:
# 		flash("All fields are required. Please try again")
# 		return redirect(url_for('main'))
# 	else:
# 		g.db = connect_db()
# 		g.db.execute('insert into posts (title, post) values (?, ?)', [request.form['title'], request.form['post']])
# 		g.db.commit()
# 		g.db.close()
# 		flash('New entry was successfully posted!')
# 		return redirect(url_for('main'))

# @app.route('/logout')
# def logout():
# 	session.pop('logged_in', None)
# 	flash('You were logged out')
# 	return redirect(url_for('login'))

if __name__ == '__main__':
	app.run(debug=True)