from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property
from . import db

class Progress(db.Model):
    __tablename__ = "progress"

    # progress properties
    _id = db.Column('id', db.Integer, primary_key=True)
    _scout_id = db.Column('scout_id', db.Integer, db.ForeignKey('user.id'), nullable=False)
    _scout = db.relationship('User', back_populates='progress', foreign_keys=[_scout_id])
    _area = db.Column('area', db.String(128), nullable=False)
    _trilho = db.Column('trilho', db.String(128), nullable=True)
    _description = db.Column('description', db.String(128), nullable=False)
    _validated_by_id = db.Column('validated_by', db.Integer, db.ForeignKey('user.id'), nullable=False)
    _validated_by = db.relationship('User', back_populates='validated_progress', foreign_keys=[_validated_by_id])

    # additional properties
    _created_at = db.Column('created_at', db.DateTime, default=datetime.utcnow)
    _updated_at = db.Column('updated_at', db.DateTime, onupdate=datetime.utcnow)
    _deleted_at = db.Column('deleted_at', db.DateTime)

    # Constructor
    def __init__(self, scout, area, description, validated_by, trilho=None):
        self._scout = scout
        self._area = area
        self._trilho = trilho
        self._description = description
        self._validated_by = validated_by

 # Getters
    @hybrid_property
    def id(self):
        return self._id

    @hybrid_property
    def scout(self):
        return self._scout

    @hybrid_property
    def area(self):
        return self._area

    @hybrid_property
    def trilho(self):
        return self._trilho

    @hybrid_property
    def description(self):
        return self._description

    @hybrid_property
    def validated_by(self):
        return self._validated_by

    @hybrid_property
    def created_at(self):
        return self._created_at

    @hybrid_property
    def updated_at(self):
        return self._updated_at

    @hybrid_property
    def deleted_at(self):
        return self._deleted_at

    # Setters
    @scout.setter
    def scout(self, scout):
        self._scout = scout

    @area.setter
    def area(self, area):
        self._area = area

    @trilho.setter
    def trilho(self, trilho):
        self._trilho = trilho

    @description.setter
    def description(self, description):
        self._description = description

    @validated_by.setter
    def validated_by(self, validated_by):
        self._validated_by = validated_by

    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at

    @updated_at.setter
    def updated_at(self, updated_at):
        self._updated_at = updated_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        self._deleted_at = deleted_at
    # Additional methods...
