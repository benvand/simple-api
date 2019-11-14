from app import db


class Recipe(db.Model):
    name = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return '<Recipe %r>' % self.name