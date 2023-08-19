from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from project.models.user import User
from project.models.progress import Progress