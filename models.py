from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

bcrypt = Bcrypt()


def connect_db(app):
    """Connect to database."""
    with app.app_context():
        db.app = app
        db.init_app(app)


class User(db.Model):
    '''model to create users'''
    
    __tablename__ = 'users'

    username = db.Column(db.String(20), nullable=False, primary_key=True, unique=True)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(50),nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30),nullable=False)


    @classmethod 
    def register(cls, username, pwd,first_name, last_name, email):

        hashed = bcrypt.generate_password_hash(pwd)
        hashed_utf8 = hashed.decode("utf8")

        return cls(username=username, password=hashed_utf8, email=email, first_name=first_name, last_name=last_name)


    def __repr__(self):

        p = self
        return f'username: {p.username}, password:{p.password}, first_name:{p.first_name}, last_name:{p.last_name} '

    