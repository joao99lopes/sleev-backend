from datetime import datetime

from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import generate_password_hash, check_password_hash

from . import db


class User(db.Model):
    __tablename__ = "user"

    # base user properties
    _id = db.Column('id', db.Integer, primary_key=True)
    _first_name = db.Column('first_name', db.String(128), nullable=False)
    _last_name = db.Column('last_name', db.String(128), nullable=False)
    _email = db.Column('email', db.String(128), nullable=True)
    _domain = db.Column('domain', db.String(128), nullable=False)
    _password_hash = db.Column('password_hash', db.String(128), nullable=False)

    # scout properties
    _scout_id = db.Column('scout_id', db.Integer, nullable=False) #equivalent to NIN
    _totem = db.Column('totem', db.String(128))
    _date_of_birth = db.Column('date_of_birth', db.DateTime, nullable=False)
    _scout_group = db.Column('scout_group', db.Integer, nullable=False) #agrupamento
    _section = db.Column('section', db.Integer, nullable=False) #secção
    _team = db.Column('team', db.String(128))
    _role = db.Column('role', db.String(128), default='scout')

    # additional properties
    _created_at = db.Column('created_at', db.DateTime, default=datetime.utcnow())
    _updated_at = db.Column('updated_at', db.DateTime, onupdate=datetime.utcnow())
    _deleted_at = db.Column('deleted_at', db.DateTime)




    def __init__(self, first_name:str, last_name:str, email:str, password:str, scout_id:int, date_of_birth:datetime, scout_group:int, section:int, role:str='scout'):
        assert User.is_valid_email(email)
        email_split:list = email.split("@")
        assert User.is_password_valid(password)

        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._domain = email_split[1]
        self.set_password(password)

        self._scout_id = scout_id
        self._date_of_birth = date_of_birth
        self._scout_group = scout_group
        self._section = section
        self._role = role

    def __str__(self) -> str:
        return f"User: id={self.id}, " \
               f"email={self.email}, " \
               f"domain={self.domain}, " \
               f"date_of_birth={self.date_of_birth}, " \
               f"scout_id={self.scout_id}, " \
               f"totem={self.totem}, " \
               f"scout_group={self.scout_group}, " \
               f"section={self.section}, " \
               f"team={self.team}, " \
               f"role={self.role}, " \
               f"created_at={self.created_at}, " \
               f"updated_at={self.updated_at}, " \
               f"deleted_at={self.deleted_at}"

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "username": self._username,
            "email": self._email,
            "domain": self._domain,
            "date_of_birth": self.date_of_birth,
            "scout_id": self.scout_id,
            "totem": self.totem,
            "scout_group": self.scout_group,
            "section": self.section,
            "team": self.team,
            "role": self.role,
            "created_at": self._created_at,
            "updated_at": self._updated_at,
            "deleted_at": self._deleted_at
        }


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
    
    @hybrid_property
    def scout_id(self) -> int:
        return self._scout_id

    @hybrid_property
    def date_of_birth(self) -> datetime:
        return self._date_of_birth

    @hybrid_property
    def scout_group(self) -> int:
        return self._scout_group

    @hybrid_property
    def section(self) -> str:
        return self._section

    @hybrid_property
    def role(self) -> str:
        return self._role

    @hybrid_property
    def totem(self) -> str:
        return self._totem

    @hybrid_property
    def team(self) -> str:
        return self._team


    ####
    # setters
    ##

    @first_name.setter
    def first_name(self, first_name:str) -> None:
        self._first_name = first_name

    @last_name.setter
    def last_name(self, last_name:str) -> None:
        self._last_name = last_name

    @email.setter
    def email(self, email:str) -> None:
        self._email = email

    @domain.setter
    def domain(self, domain:str) -> None:
        self._domain = domain

    @password_hash.setter
    def password_hash(self, password_hash:str) -> None:
        self._password_hash = password_hash

    @deleted_at.setter
    def deleted_at(self, deleted_at:datetime) -> None:
        self._deleted_at = deleted_at

    @scout_group.setter
    def scout_group(self, scout_group:int) -> None:
        self._scout_group = scout_group
        
    @section.setter
    def section(self, section:str) -> None:
        self._section = section
        
    @role.setter
    def role(self, role:str) -> None:
        self._role = role
        
    @totem.setter
    def totem(self, totem:str) -> None:
        self._totem = totem
        
    @team.setter
    def team(self, team:str) -> None:
        self._team = team
        

####
# aux
##
    def delete(self):
        self.deleted_at = datetime.now()
        db.session.commit()

    def set_password(self, password:str) -> None:
        if User.is_password_valid(password):
            self._password_hash = generate_password_hash(password)

    def check_password(self, password:str) -> bool:
        return check_password_hash(self._password_hash, password)

    def is_password_valid(password:str) -> bool:
        # TODO.txt:add an evaluator
        return len(password) > 4

    def is_valid_email(email:str) -> bool:
        # TODO.txt: add an evaluator
        return "@" in email


