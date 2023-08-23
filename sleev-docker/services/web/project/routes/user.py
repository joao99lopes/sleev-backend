from flask import request
from datetime import datetime

from project.api.user import *
from . import users_blueprint


@users_blueprint.route("/new", methods=['POST'])
def new_user():
    try:
        data = request.get_json()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password_string = data.get('password')
        scout_id = data.get('scout_id')
        scout_group = data.get('scout_group')
        birth_date = datetime.fromisoformat(data.get('birth_date'))
        section = data.get('section')
        role = data.get('role')
    except ValueError as e:
        return jsonify({
            "msg": "An error occurred retrieving data from json",
            "error": e.__str__(),
            "success": False,
            "data": ""
        }), 400
    
    return add_user(first_name=first_name, last_name=last_name, email=email, password_str=password_string, birth_date=birth_date, role=role, scout_group=scout_group, scout_id=scout_id, section=section)

@users_blueprint.route("/delete", methods=['POST'])
def delete():
    data = request.get_json()
    email = data.get('email')
    return delete_user(email)

@users_blueprint.route("/delete_all", methods=['POST'])
def delete_all():
    return delete_all_users()

@users_blueprint.route("/migrate", methods=['POST'])
def migrate_users():
    return migrate_users()
