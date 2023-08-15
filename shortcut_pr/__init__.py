from flask import Flask
import pymongo
from dotenv import dotenv_values
import os
config = dotenv_values('.env')
mongo = pymongo.MongoClient(config['MONGO_URI'])
db = pymongo.database.Database(mongo, config['DB_NAME'])
col = pymongo.collection.Collection(db, config['DB_COLLECTION'])
SECRET_KEY = os.urandom(32)


def create_app(config_object='shortcut_pr.settings'):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    from shortcut_pr.main.routes import main
    from shortcut_pr.add.routes import add
    from shortcut_pr.dashboard.routes import dashboard
    app.register_blueprint(main)
    app.register_blueprint(add)
    app.register_blueprint(dashboard)
    return app
