import os

from flask import Flask, jsonify
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object("project.config.Config")

migrate = Migrate()

# Initialize Flask extensions here
from project.routes import users_blueprint

app.register_blueprint(blueprint=users_blueprint)


# Register blueprints here


# App main route
@app.route("/")
def hello_world():
    return jsonify({
        "msg": "hello world",
        "success": True,
        "data": None
    }), 200


# Start the app (only runs on boot)
APP_STARTED = os.getenv("APP_STARTED")
if APP_STARTED != "1":
    from project.models import db

    db.init_app(app)
    migrate.init_app(app, db)
    os.environ["APP_STARTED"] = "1"
