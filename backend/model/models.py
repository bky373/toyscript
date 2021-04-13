from db.init_db import db


class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    name = db.Column(db.String(50))
    frequency = db.Column(db.Integer)
    __table_args__ = {"extend_existing": True}


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    name = db.Column(db.String(50))
    lines = db.Column(db.Integer)
    __table_args__ = {"extend_existing": True}


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200))
    author = db.Column(db.String(100))
    total_characters = db.Column(db.Integer)
    total_pages = db.Column(db.Integer)
    total_places = db.Column(db.Integer)
    total_scenes = db.Column(db.Integer)
    __table_args__ = {"extend_existing": True}


class Scene(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    num = db.Column(db.Integer, unique=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    place_id = db.Column(db.Integer, db.ForeignKey("place.id"))
    place = db.relationship("Place")
    time_id = db.Column(db.Integer, db.ForeignKey("time.id"))
    time = db.relationship("Time")
    __table_args__ = {"extend_existing": True}


class Line(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    character_id = db.Column(db.Integer, db.ForeignKey("character.id"))
    character = db.relationship("Character")
    line = db.Column(db.Text)

class Time(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    frequency = db.Column(db.Integer)
    __table_args__ = {"extend_existing": True}


class TimeCharacter(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    time_id = db.Column(db.Integer, db.ForeignKey("time.id"))
    time = db.relationship("Time")
    character_id = db.Column(db.Integer, db.ForeignKey("character.id"))
    character = db.relationship("Character")
    frequency = db.Column(db.Integer)
    __table_args__ = {"extend_existing": True}


class PlaceCharacter(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    place_id = db.Column(db.Integer, db.ForeignKey("place.id"))
    character_id = db.Column(db.Integer, db.ForeignKey("character.id"))
    character = db.relationship("Character")
    frequency = db.Column(db.Integer)
    __table_args__ = {"extend_existing": True}

class Sentiment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    character_id = db.Column(db.Integer, db.ForeignKey("character.id"))
    character = db.relationship("Character")
    positive = db.Column(db.Integer)
    anticipation = db.Column(db.Integer)
    trust = db.Column(db.Integer)
    negative = db.Column(db.Integer)
    joy = db.Column(db.Integer)
    fear = db.Column(db.Integer)
    sadness = db.Column(db.Integer)
    anger = db.Column(db.Integer)
    surprise = db.Column(db.Integer)
    disgust = db.Column(db.Integer)

class Network(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    charac_one_id = db.Column(db.Integer, db.ForeignKey("character.id"))
    charac_two_id = db.Column(db.Integer, db.ForeignKey("character.id"))
    value = db.Column(db.Integer)