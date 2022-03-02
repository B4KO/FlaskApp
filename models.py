from app import db
from datetime import datetime, timedelta
class Book(db.Model):
    __tablename__ = "book"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    release = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    
    reviews = db.relationship('Review', backref='book', lazy = 'dynamic')
    
    def __repr__(self):
        return "This is {0}".format(self.name)
    
class Author(db.Model):
    __tablename__ = "author"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,  nullable=False)
    birthdate = db.Column(db.DateTime, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    
    books = db.relationship('Books', backref='authors_books', lazy=True)
    

class Review(db.Model):
    __tablename__ = "review"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
   
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
   

class User(db.Model):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    birthdate = db.Column(db.DateTime, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    
    reviews = db.relationship('Review', backref='reviewer', lazy = 'dynamic')
