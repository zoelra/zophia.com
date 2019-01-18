from program import db


class Post(db.Model):
    __tablename__ = 'posts'

    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    post = db.Column(db.String, nullable=False)
    post_date = db.Column(db.Date, nullable=False)

    def __init__(self, title, post, post_date):
        self.title = title
        self.post = post
        self.post_date = post_date

    def __repr__(self):
        return '<title {0}'.format(self.title)
