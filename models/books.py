from flask_app import db

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author_name = db.Column(db.String(50), nullable=True)
    author_surname = db.Column(db.String(50), nullable=True)
    month = db.Column(db.String(2))
    year = db.Column(db.Integer)

    def __repr__(self):
        return f"Book('{self.id}', '{self.title}', '{self.author_name}', '{self.author_surname}', '{self.month}', '{self.year}')"