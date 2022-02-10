import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Primarykey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

Class People()
__tablename__="people"
    id= db.Column(Integer, primary_key=True)
    name= db.Column(String(200))
    height= db.Column(Integer(100))
    mass= db.Column(Integer(200))
    gender= db.Column(String(50))
    birth_year= db.Column(Integer(50))
    people_id= db.Column(Integer, ForeignKey('people.id'))

Class Planets()    
__tablename__="planets"
    id= db.Column(Integer, primary_key=True)
    name= db.Column(String(200))
    mass= db.Column(Integer(200))
    climate= db.Column(String(200))
    orbit= db.Column(Integer(200))
    gravity= db.Column(Integer(200))
    terrain= db.Column(String(200))
    population= db.Column(Integer(200))
    planets_id= db.Column(Integer, ForeignKey('planets.id'))

Class Favourites()
__tablename__="favourites"
    id= db.Column(Integer, primary_key=True)
    name= db.Column(String(200))
    favourites_id(db.Column(Integer,ForeignKey("favourites_id"))

Class User()
__tablename__="user"
    id = db.Column('user_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   password = db.Column(db.String(50))  
   pin = db.Column(db.Integer(10))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')