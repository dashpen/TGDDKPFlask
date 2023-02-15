import os
from __init__ import db, app
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import Blueprint, request, jsonify

class BattleshipUsers(UserMixin, db.Model):
    __tablename__ = 'battleship_users'
    
    # Define the Users schema
    username = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.String(255), unique=False, nullable=False)
    # Defines a relationship between User record and Notes table, one-to-many (one user to many notes)
    # notes = db.relationship("Notes", cascade='all, delete', backref='users', lazy=True)

    # constructor of a User object, initializes of instance variables within object
    def __init__(self, username="", score=""):
        self.username = make_id(username)
        self.score = score

    # returns a string representation of object, similar to java toString()
    def __repr__(self):
        return "Users(" + str(self.username) + "," + self.score + ")"

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
            "username": self.username,
            "score": self.score,
        }

    def read2(self):
        return {
            "username": self.username,
            "score": self.score,
        }

    # CRUD update: updates users name, password, phone
    # returns self
    def update(self, username="", score=""):
        """only updates values with length"""
        if len(username) > 0:
            self.username = username
        if len(score) > 0:
            self.score = score
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

    # required for login_user, overrides id (login_user default) to implemented userID
    def get_score(self):
        return self.score

def getUser(score):
    users = BattleshipUsers.query.all()
    for user in users:
        if(user.get_score() == score):
            return user
        
def make_id():
    users = BattleshipUsers.query.all()
    score = 0
    for user in users:
        if(user.get_score() > score):
            score = user.get_score()
    if (score < 100):
        return 100
    return score + 1

def createBattleshipTable():
    with app.app_context():
        db.init_app(app)
        db.create_all()
        u1 = BattleshipUsers(username='Toby', score="19")
        u2 = BattleshipUsers(username='Gene', score="34")
        try:
            '''add user/note data to table'''
            u1.create()
            u2.create()
        except IntegrityError:
            '''fails with bad or duplicate data'''
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {u1.username}")

if __name__ == "__main__":
    # createTestingData()
    user1 = BattleshipUsers(score="18", name="Bum")
    print(user1.username)
    # badUser = getUser(102)
    # badUser.delete()
    print("asdf")
