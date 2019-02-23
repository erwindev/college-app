from app.api.application_api import apiv1
import os
from app import create_app
from flask_script import Manager
from app.api.utility import api as utility_ns
from app.api.college import api as college_ns
from app.api.student import api as student_ns

app = create_app(os.getenv('ENV_CONFIG') or 'default')
app.register_blueprint(apiv1)
manager = Manager(app)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,PATCH,POST,DELETE')
    return response

if __name__ == '__main__':
    # Running in Non-Production mode
    import logging

    logging.basicConfig(filename='error.log', level=logging.DEBUG)
    app.run()