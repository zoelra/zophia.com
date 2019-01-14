import sqlite3

with sqlite3.connect("blog.db") as connection:
	c = connection.cursor()

	c.execute("""CREATE TABLE posts (title TEXT, post TEXT)""")

	c.execute('INSERT INTO posts VALUES("First Blog Post", "Thank you for visiting my new website.\
		It is still in development and will be changing continuously.\
		Please stay tuned for new updates and functionality. Cheers!")')
	
	