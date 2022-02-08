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

Class People()
__tablename__="people"
    id= column(Integer, primary_key=True)
    name= Column(String(200))
    height= Column(Integer(100))
    mass= Column(Integer(200))
    gender= column(String(50))
    birth_year= column(Integer(50))
    people_id= Column(Integer, ForeignKey('people.id'))

Class Planets()    
__tablename__="planets"
    id= column(Integer, primary_key=True)
    name=Column(String(200))
    mass=Column(Integer(200))
    climate= Column(String(200))
    orbit=Column(Integer(200))
    gravity=Column(Integer(200))
    terrain= Column(String(200))
    population= Column(Integer(200))
    planets_id= Column(Integer, ForeignKey('planets.id'))

Class Favourites()
__tablename__="favourites"
    id= column(Integer, primary_key=True)
    name= column(String(200))
    favourites_id(column(Integer,ForeignKey("favourites_id"))

Class User()
__tablename__="user"
    id


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')