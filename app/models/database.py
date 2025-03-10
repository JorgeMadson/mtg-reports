from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    reports = db.relationship('Report', backref='player', lazy=True)
    matches_as_opponent = db.relationship('Match', backref='opponent', lazy=True)

class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50))  # e.g., "Weekly", "Annual"
    events = db.relationship('Event', backref='place', lazy=True)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=False)
    num_players = db.Column(db.Integer)
    prizes = db.Column(db.Text)
    reports = db.relationship('Report', backref='event', lazy=True)

class Deck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    colors = db.Column(db.JSON)  # e.g., ["Black", "Green"]
    archetype = db.Column(db.String(50))  # e.g., "Aggro", "Control"
    variation = db.Column(db.String(50))  # e.g., "Kiki", "Hogaak"
    cards = db.Column(db.JSON)  # List of card names
    reports = db.relationship('Report', backref='deck', lazy=True)
    matches = db.relationship('Match', backref='opponent_deck', lazy=True)

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    deck_id = db.Column(db.Integer, db.ForeignKey('deck.id'), nullable=False)
    final_standing = db.Column(db.Integer)
    prize = db.Column(db.String(100))
    notes = db.Column(db.Text)
    matches = db.relationship('Match', backref='report', lazy=True)

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    report_id = db.Column(db.Integer, db.ForeignKey('report.id'), nullable=False)
    opponent_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    opponent_deck_id = db.Column(db.Integer, db.ForeignKey('deck.id'), nullable=False)
    games_won = db.Column(db.Integer, nullable=False)
    games_lost = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text)
    games = db.relationship('Game', backref='match', lazy=True)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), nullable=False)
    game_number = db.Column(db.Integer, nullable=False)
    won = db.Column(db.Boolean, nullable=False)
    mulligans = db.Column(db.Integer)
    key_plays = db.Column(db.Text)
    mistakes = db.Column(db.Text)
    improvements = db.Column(db.Text)