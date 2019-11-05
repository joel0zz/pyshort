from . import db


class Url(db.Model):
    __tablename__ = 'urls'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(128), unique=True, index=True)
    short_url = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<Url %r>' % self.url
