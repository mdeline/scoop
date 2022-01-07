from . import db

class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(50),
        index=True,
        unique=False,
        nullable=False
    )
    description = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=True
    )
    address = db.Column(
        db.Text,
        index=False,
        unique=False,
        nullable=False
    )

    def __repr__(self):
        return '<Restaurant {}>'.format(self.name)