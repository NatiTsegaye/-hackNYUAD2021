from flask_restful import Api
from flask import Flask
import os
from Main.Routes.routes import initialize_routes
from config import Config
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)


app.config['MONGODB_SETTINGS'] = {
    'host': Config.DB
}

CORS(app, resources={r'/*':{"origins": "*"}},allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Methods"])

from Main.DAC.config import initialize_db
initialize_db(app)
initialize_routes(api)
