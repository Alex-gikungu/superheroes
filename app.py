from flask import Flask
from config import Config
from models import db
from flask_migrate import Migrate
from flask_restful import Api, Resource

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)
from routes import *

if __name__ == '__main__':
    app.run(debug=True)
