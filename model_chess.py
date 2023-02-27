import os
from __init__ import db, app
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin
from flask import Blueprint, request, jsonify
from model_battleship import BattleshipUsers


class ChessUsers(UserMixin, db.Model):
    __tablename__ = 'chess_users'
    
    # Define the Users schema
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    dob = db.Column(db.String(255), unique = False, nullable=False)
    games = db.Column(db.String(255), unique = False, nullable=False)
    # Defines a relationship between User record and Notes table, one-to-many (one user to many notes)
    # notes = db.relationship("Notes", cascade='all, delete', backref='users', lazy=True)

    # constructor of a User object, initializes of instance variables within object
    def __init__(self, name, uid="0", password="null", dob="11-11-1111", games=""):
        self.uid = make_id()
        self.name = name
        self.dob = dob
        self.games = ""
        self.set_password(password)

    # returns a string representation of object, similar to java toString()
    def __repr__(self):
        return "Users(" + str(self.uid) + "," + self.name + "," + str(self.dob) +  str(self.games) + ")"

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from Users(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "uid": self.uid,
            "name": self.name,
            "password": self.password,
            "dob": self.dob,
            "games": self.games
        }

    def read2(self):
        return {
            "uid": self.uid,
            "name": self.name,
            "dob": self.dob,
        }

    # CRUD update: updates users name, password, phone
    # returns self
    def update(self, name="", uid="", password="", dob=""):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(uid) > 0:
            self.uid = uid
        if len(password) > 0:
            self.set_password(password)
        if len(dob) > 0:
            self.dob = dob
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

    def deleteGame(self, gameID):
        print(self.games)

    # set password method is used to create encrypted password
    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    # check password to check versus encrypted password
    def is_password_match(self, password):
        """Check hashed password."""
        result = check_password_hash(self.password, password)
        return result

    # required for login_user, overrides id (login_user default) to implemented userID
    def get_id(self):
        return self.uid

    def update_games(self, game):
        self.games += "#" + str(game)
        try:
            db.session.commit()
            return self
        except IntegrityError:
            db.session.remove()
            return None

def getUser(uid):
    users = ChessUsers.query.all()
    for user in users:
        if(user.get_id() == uid):
            return user

def getName(name):
    user = ChessUsers.query.all()
    for user in name:
        if(user.get_name() == name):
            return name
        
def make_id():
    users = ChessUsers.query.all()
    uid = 0
    for user in users:
        if(user.get_id() > uid):
            uid = user.get_id()
    if (uid < 100):
        return 100
    return uid + 1

def getGame(uid, date):
    user = getUser(uid)
    games = user.games.split('#')
    for game in games:
        if game.date == date:
            return game
    
def createTestingData():
    with app.app_context():
        db.init_app(app)
        db.create_all()
        u1 = ChessUsers(name='Toby', password="lmaobad", uid="12")
        u2 = ChessUsers(name='Gene', password="WRizz", uid="123")
        u3 = BattleshipUsers(username='das', score="19")
        u4 = BattleshipUsers(username='parav', score="34")
        try:
            '''add user/note data to table'''
            u1.create()
            u2.create()
            u3.create()
            u4.create()
            u5.create()
            u6.create()
        except IntegrityError:
            '''fails with bad or duplicate data'''
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {u1.uid}")

if __name__ == "__main__":
    createTestingData()
    
