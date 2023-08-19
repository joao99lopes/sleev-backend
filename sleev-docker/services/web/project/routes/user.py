from flask import request

from project.api.user import *
from . import users_blueprint


@users_blueprint.route("/new", methods=['POST'])
def new_user():
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password_string = data.get('password')
    return add_user(first_name, last_name, email, password_string)


@users_blueprint.route("/delete", methods=['POST'])
def delete():
    data = request.get_json()
    email = data.get('email')
    return delete_user(email)

@users_blueprint.route("/delete_all", methods=['POST'])
def delete_all():
    return delete_all_users()
