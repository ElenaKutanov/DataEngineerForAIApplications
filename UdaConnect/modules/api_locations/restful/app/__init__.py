from flask import Flask, jsonify, Blueprint, send_from_directory
from flask_cors import CORS
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy

from flask_swagger_ui import get_swaggerui_blueprint

db = SQLAlchemy()


def create_app(env=None):
    from app.config import config_by_name
    from app.routes import register_routes

    SWAGGER_URL = '/doc'
    API_URL = '/docs/swagger.json'

    doc_api_blueprint  = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={ "app_name": "Udaconnect" } 
    )

    app = Flask(__name__)

    app.register_blueprint(doc_api_blueprint, url_prefix=SWAGGER_URL)

    @app.route('/docs/<path:path>')
    def send_report(path):
        return send_from_directory('/docs', path)

    app.config.from_object(config_by_name[env or "test"])

    api = Api(app, title="UdaConnect API", version="0.1.0")

    CORS(app)  # Set CORS for development

    register_routes(api, app)
    db.init_app(app)

    @app.route("/health")
    def health():
        return jsonify("healthy")

    return app
