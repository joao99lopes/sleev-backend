from flask import jsonify, Blueprint

users_blueprint: Blueprint = Blueprint("user", __name__, url_prefix="/user")
progress_blueprint: Blueprint = Blueprint("progress", __name__, url_prefix="/progress")

from . import user, progress
