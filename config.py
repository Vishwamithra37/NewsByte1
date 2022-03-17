from apispec_webframeworks.flask import FlaskPlugin
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec import APISpec
from flask_apispec import FlaskApiSpec
import flask

app = flask.Flask(__name__)
app.app_context().push()
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='NewsBytes_VishwaMithra',
        version='v1',
        plugins=[FlaskPlugin(),MarshmallowPlugin()],
        openapi_version='3.0.2',
        info={
            'description': 'This is NewBytes_VishwaMithra',
            'contact': { 'name': 'Vishwa Mithra', 'email': 'mithravishwa37@gmail.com',"mobile":"+91-9888888888" },
            'license': { 'name': 'MIT'}
        }
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',
})
docs = FlaskApiSpec(app)