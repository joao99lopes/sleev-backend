from flask import request
from datetime import datetime

from project.api.progress.progress import get_progress_from_user_id

from project.api.user import *
from . import progress_blueprint


@progress_blueprint.route("/get_personal", methods=['POST'])
def get_personal_progress():
    try:
        data = request.get_json()
        user_token = data.get('user_token')
        user_id = data.get('user_id')
    except ValueError as e:
        return jsonify({
            "msg": "An error occurred retrieving data from json",
            "error": e.__str__(),
            "success": False,
            "data": ""
        }), 400
    
    return get_progress_from_user_id(user_id=user_id)

