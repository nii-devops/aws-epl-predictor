from app import db
from flask_login import UserMixin



# User Model
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    nickname = db.Column(db.String(30) )
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120))
    
    picture = db.Column(db.String())

    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<User {self.username}>'

    # Establishing relationships
    predictions = db.relationship('Prediction', back_populates='user', cascade='all, delete-orphan')  # Added cascade
    scores = db.relationship('Score', back_populates='user', cascade='all, delete-orphan')  # Added cascade


# Week Model
class Week(db.Model):
    __tablename__ = 'weeks'  # Define table name
    id          = db.Column(db.Integer, primary_key=True)
    week_number = db.Column(db.Integer, unique=True, nullable=False)
    
    # Establishing relationships
    fixtures    = db.relationship('Fixture', back_populates='week', cascade='all, delete-orphan')  # Added cascade
    predictions  = db.relationship('Prediction', back_populates='week', cascade='all, delete-orphan')  # Added cascade
    results     = db.relationship('Result', back_populates='week', cascade='all, delete-orphan')  # Added cascade
    scores      = db.relationship('Score', back_populates='week', cascade='all, delete-orphan')  # Added cascade


# Fixture Model
class Fixture(db.Model):
    __tablename__ = 'fixtures'  # Define table name
    id          = db.Column(db.Integer, primary_key=True)
    week_id     = db.Column(db.Integer, db.ForeignKey('weeks.id'), nullable=False)
    matches     = db.Column(db.JSON, nullable=False)
    # date_created = db.Column(db.String, nullable=False)
    # Establishing relationships
    week        = db.relationship('Week', back_populates='fixtures')  # Updated to back_populates



# Prediction Model
class Prediction(db.Model):
    __tablename__ = 'predictions'  # Define table name
    id                  = db.Column(db.Integer, primary_key=True)
    user_id             = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    week_id             = db.Column(db.Integer, db.ForeignKey('weeks.id'), nullable=False)
    user_predictions    = db.Column(db.JSON, nullable=False)
    # date_submitted = db.Column(db.String, nullable=False)

    # Establishing relationships
    user                = db.relationship('User', back_populates='predictions')  # Updated to back_populates
    week                = db.relationship('Week', back_populates='predictions')  # Updated to back_populates



# Results Model
class Result(db.Model):
    __tablename__ = 'results'  # Define table name
    id      = db.Column(db.Integer, primary_key=True)
    week_id = db.Column(db.Integer, db.ForeignKey('weeks.id'), nullable=False)
    results = db.Column(db.JSON, nullable=False)
    # date_submitted = db.Column(db.String, nullable=False)

    # Establishing relationships
    week    = db.relationship('Week', back_populates='results', cascade='all, delete-orphan', single_parent=True)  # Added single_parent=True



# Score Model
class Score(db.Model):
    __tablename__ = 'scores'  # Define table name
    id          = db.Column(db.Integer, primary_key=True)
    user_id     = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    week_id     = db.Column(db.Integer, db.ForeignKey('weeks.id'), nullable=False)
    points      = db.Column(db.Integer, default=0)

    # Relationships
    user        = db.relationship('User', back_populates='scores')  # Updated to back_populates
    week        = db.relationship('Week', back_populates='scores')  # Updated to back_populates


# Score Model
class Xrecord(db.Model):
    __tablename__ = 'xrecords'  # Define table name
    
    id          = db.Column(db.Integer, primary_key=True)
    name     = db.Column(db.String, nullable=False)
    points      = db.Column(db.Integer, default=0)





