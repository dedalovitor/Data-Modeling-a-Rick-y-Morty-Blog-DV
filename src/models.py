import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    last_name = Column(String(250))
    gender = Column(String(250))
    species = Column(String(250))

class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    type = Column(String(250))
    dimension = Column(String(250))

class Episode(Base):
    __tablename__ = 'episode'
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    air_date = Column(String(250))
    episode = Column(String(250))


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    character = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    location_id = Column(Integer, ForeignKey('location.id'))
    location = relationship(Location)
    episode_id = Column(Integer, ForeignKey('episode.id'))
    episode = relationship(Episode)

class LocationsAndEpisodes(Base):
    __tablename__ = 'locationsandepisodes'
    id = Column(Integer, primary_key=True)
    location_id = Column(Integer, ForeignKey('location.id'))
    location = relationship(Location)
    episode_id = Column(Integer, ForeignKey('episode.id'))
    episode = relationship(Episode)

class EpisodesAndCharacters(Base):
    __tablename__ = 'episodesandcharacters'
    id = Column(Integer, primary_key=True)
    episode_id = Column(Integer, ForeignKey('episode.id'))
    episode = relationship(Episode)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
