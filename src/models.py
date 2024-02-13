import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    fecha_subscripcion = Column(String(250), nullable= False)

class Planeta(Base):
    __tablename__ = 'planeta'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(Enum('humedo', 'arido','seco'), nullable=False)
    terrain = Column(Enum('gaseoso','nevado','desertico'), nullable=False)
    population = Column(Integer, nullable=False)

class Personaje(Base):
    __tablename__ = 'personaje'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250),nullable=False)
    last_name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    hair_color = Column(Enum('negro','blanco','rubio'))
    eye_color = Column(Enum('negro','azul','marron','verde'))
    planeta_id = Column(Integer,ForeignKey('planeta.id'))

class Favorito(Base):
    __tablename__ = 'favorito'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_favorito = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'))
    id_planeta = Column(Integer, ForeignKey('planeta.id'))
    id_personaje = Column(Integer, ForeignKey('personaje.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
