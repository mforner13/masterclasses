from app import db


class User(db.Model):   # User inherits from db.Model, a base class for all models from Flask-sqlalchemy
    id = db.Column(db.Integer, primary_key=True)    # Fields are created as instances of the Column class, they take the field type as an argument
    email = db.Column(db.String(120), index=True, unique=True)  # By indexing a value you can find it more easily in the db
    first_name = db.Column(db.String(50), index=True, unique=False) # Do I need to say when something shouldn't be unique? Or just leave it?
    last_name = db.Column(db.String(50), index=True, unique=False)
    password_hash = db.Column(db.String(128))
    masterclasses = db.relationship('MasterclassInstance', backref='instructor', lazy='dynamic')
    booked_masterclasses = db.relationship('MasterclassAttendee', backref='attendee', lazy='dynamic')

    def __repr__(self):
        return '<User {} {}>'.format(self.first_name, self.last_name)


class Masterclass(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime, index=True)
    masterclass_instances = db.relationship('MasterclassInstance', backref='location', lazy='dynamic')


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    building = db.Column(db.String(50), index=True)
    street_number = db.Column(db.String(10)) # should keep numbers as strings unless going to do calculations?
    street_name = db.Column(db.String(100), index=True)
    town_or_city = db.Column(db.String(50), index=True)
    postcode = db.Column(db.String(8), index=True)  # A postcode in the UK can't have more than 8 characters inc. space
    masterclass_instances = db.relationship('MasterclassInstance', backref='location', lazy='dynamic')


class MasterclassInstance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True)
    masterclass_id = db.Column(db.Integer, db.ForeignKey('masterclass.id'))
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    instructor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #  How do I represent attendees - many to many relationship

class MasterclassAttendee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    attendee_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    masterclass_id = db.Column(db.Integer, db.ForeignKey('masterclass.id'))
