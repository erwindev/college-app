from flask import Flask
from config import config
from flask_nameko import FlaskPooledClusterRpcProxy

rpc = FlaskPooledClusterRpcProxy()

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app, config_name)

    app.config.update(dict(
        NAMEKO_AMQP_URI='amqp://localhost'
    ))    

    rpc.init_app(app)

    return app
