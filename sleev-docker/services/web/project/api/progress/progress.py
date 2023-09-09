from flask import jsonify

from project.api.user import get_user_from_id
from project.models import User, Progress


def get_progress_from_id(user_id: int):
    return Progress.query.filter_by(user_id=user_id)


def get_progress_from_user_id(user_id:int):
    user: User = get_user_from_id(user_id=user_id)
    if (user is None):
        return jsonify({
            "msg": "",
            "error": "user does not exist",
            "success": False,
            "data": ""
        }), 409
    
    user_progress = get_progress_from_id(user_id)