import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
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

class People(Base):
    __tablename__="people"
    id= Column(Integer, primary_key=True)
    name= Column(String(200))
    height= Column(Integer)
    mass= Column(Integer)
    gender= Column(String(50))
    birth_year= Column(Integer)

class Planets(Base):   
    __tablename__="planets"
    id= Column(Integer, primary_key=True)
    name= Column(String(200))
    mass= Column(Integer)
    climate= Column(String(200))
    orbit= Column(Integer)
    gravity= Column(Integer)
    terrain= Column(String(200))
    population= Column(Integer)

class FavouritePlanets(Base):
    __tablename__="favouriteplanets"
    id= Column(Integer, primary_key=True)
    name= Column(String(200))
    user_id= Column(Integer, ForeignKey('user.id'))
    planets_id= Column(Integer, ForeignKey('planets.id'))
    FavouritePlanets = relationship(user_id)


class FavouritePeople(Base):
    __tablename__="favouritepeople"
    id= Column(Integer, primary_key=True)
    name= Column(String(200))
    user_id= Column(Integer, ForeignKey('user.id'))
    people_id= Column(Integer, ForeignKey('people.id'))
    FavouritePeople = relationship(user_id)


class User(Base):
    __tablename__="user"
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    password = Column(String(50))  


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')