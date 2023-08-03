from flask import jsonify, Blueprint

users_blueprint: Blueprint = Blueprint("user", __name__, url_prefix="/user")


@users_blueprint.route("/")
def users_index():
    return jsonify(src="users")


from . import user
