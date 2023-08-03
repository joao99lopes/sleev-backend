from datetime import datetime

from sqlalchemy import desc
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import generate_password_hash, check_password_hash

from . import db


class User(db.Model):
    __tablename__ = "user"

    _id = db.Column('id', db.Integer, primary_key=True)
    _first_name = db.Column('first_name', db.String(128), nullable=False)
    _last_name = db.Column('last_name', db.String(128), nullable=False)
    _username = db.Column('username', db.String(128), unique=True)
    _email = db.Column('email', db.String(128), nullable=False)
    _domain = db.Column('domain', db.String(128), nullable=False)
    _password_hash = db.Column('password_hash', db.String(128), nullable=False)
    _created_at = db.Column('created_at', db.DateTime, default=datetime.utcnow())
    _updated_at = db.Column('updated_at', db.DateTime, onupdate=datetime.utcnow())
    _deleted_at = db.Column('deleted_at', db.DateTime)

    def __init__(self, first_name: str, last_name: str, email: str, password: str):
        assert User.is_valid_email(email)
        email_split: list = email.split("@")
        assert User.is_password_valid(password)

        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._domain = email_split[1]
        self.set_password(password)

    def set_password(self, password: str) -> None:
        if User.is_password_valid(password):
            self._password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self._password_hash, password)

    def is_password_valid(password: str) -> bool:
        # TODO: add an evaluator
        return len(password) > 4

    def is_valid_email(email: str) -> bool:
        # TODO: add an evaluator
        return "@" in email

    ####
    # getters
    ##

    @hybrid_property
    def id(self) -> int:
        return self._id

    @hybrid_property
    def first_name(self) -> str:
        return self._first_name

    @hybrid_property
    def last_name(self) -> str:
        return self._last_name

    @hybrid_property
    def username(self) -> str:
        return self._username

    @hybrid_property
    def email(self) -> str:
        return self._email

    @hybrid_property
    def domain(self) -> str:
        return self._domain

    @hybrid_property
    def password_hash(self) -> str:
        return self._password_hash

    @hybrid_property
    def created_at(self) -> datetime:
        return self._created_at

    @hybrid_property
    def updated_at(self) -> datetime:
        return self._updated_at

    @hybrid_property
    def deleted_at(self) -> datetime:
        return self._deleted_at

    ####
    # setters
    ##

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        self._first_name = first_name

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        self._last_name = last_name

    @username.setter
    def username(self, username: str) -> None:
        self._username = username

    @email.setter
    def email(self, email: str) -> None:
        self._email = email

    @domain.setter
    def domain(self, domain: str) -> None:
        self._domain = domain

    @password_hash.setter
    def password_hash(self, password_hash: str) -> None:
        self._password_hash = password_hash

    @updated_at.setter
    def updated_at(self, updated_at: datetime) -> None:
        self._updated_at = updated_at

    @deleted_at.setter
    def deleted_at(self, deleted_at: datetime) -> None:
        self._deleted_at = deleted_at

    def __str__(self) -> str:
        return f"User: id={self._id}, " \
               f"username={self._username}, " \
               f"email={self._email}, " \
               f"domain={self._domain}, " \
               f"created_at={self._created_at}, " \
               f"updated_at={self._updated_at}, " \
               f"deleted_at={self._deleted_at}"

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "username": self._username,
            "email": self._email,
            "domain": self._domain,
            "created_at": self._created_at,
            "updated_at": self._updated_at,
            "deleted_at": self._deleted_at
        }

    def delete(self):
        self.deleted_at = datetime.now()
        db.session.commit()
