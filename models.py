from app import db


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    post = db.Column(db.String())

    def __init__(self, title, post):
        self.title = title
        self.post = post

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Link(db.Model):
    __tablename__ = 'link'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    link = db.Column(db.String())

    def __init__(self, title, link):
        self.title = title
        self.link = link

    def __repr__(self):
        return '<id {}>'.format(self.id)