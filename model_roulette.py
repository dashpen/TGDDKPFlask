from sqlalchemy import Column, Integer, String
from __init__ import db
from sqlalchemy.exc import IntegrityError
import random


#class Roulette(db.Model):
    #__tablename__ = "roulette"

    #id = Column(Integer, primary_key=True)
    #_user = Column(String(255), nullable=False)
    #_score = Column(Integer, nullable=False)

    #def __init__(self, user, score):
     #   self._user = user
      #  self._score = score

    #def __repr__(self):
     #   return "<Roulette(id='%s', user='%s', score='%s')>" % (
      #      self.id,
       #     self.user,
        #    self.score,
        #)

#    # @property
#     def user(self):
#         return self._user

#     @user.setter
#     def user(self, value):
#         self._user = value

#     @property
#     def score(self):
#         return self._score

#     @score.setter
#     def score(self, value):
#         self._score = value

#     def to_dict(self):
#         return {"id": self.id, "user": self.user, "score": self.score}
    
#     def create(self):
#         try:
#             # creates a person object from Users(db.Model) class, passes initializers
#             db.session.add(self)  # add prepares to persist person object to Users table
#             db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
#             return self
#         except IntegrityError:
#             db.session.remove()
#             return None
    
#     def read(self):
#         return {
#             "user": self.user,
#             "score": self.score,
#         }


# def roulettes_table_empty():
#     return len(db.session.query(Roulette).all()) == 0


# def init_roulettes():
#     if not roulettes_table_empty():
#         return

#     users_scores = [
#         ("Alice", random.randint(50, 100)),
#         ("Bob", random.randint(50, 100)),
#         ("Charlie", random.randint(50, 100)),
#         ("Dave", random.randint(50, 100)),
#         ("Eve", random.randint(50, 100)),
#     ]

#     roulettes = [Roulette(user, score) for user, score in users_scores]
#     for roulette in roulettes:
#         try:
#             db.session.add(roulette)
#             db.session.commit()
#         except Exception as e:
#             print("error while creating roulettes: " + str(e))
#             db.session.rollback()
