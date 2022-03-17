from urllib import request
from apispec_webframeworks.flask import FlaskPlugin
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec import APISpec
from flask_apispec import FlaskApiSpec
import flask

app = flask.Flask(__name__)
app.app_context().push()
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Galam',
        version='v1',
        plugins=[FlaskPlugin(),MarshmallowPlugin()],
        openapi_version='3.0.2',
        info={
            'description': 'This is a Galam backend',
            'contact': { 'name': 'Vishwa Mithra', 'email': 'mithravishwa37@gmail.com',"mobile":"+91-9888888888" },
            'license': { 'name': 'MIT'}
        }
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',
})
docs = FlaskApiSpec(app)




utm_array=["utm_source","utm_medium","utm_campaign","utm_term","utm_content"]
@app.route('/')
def index():
    for i in utm_array:
        print(flask.request.args.get(i))
    return "Hello World!"    
docs.register(target=index)


if __name__ == '__main__':
    app.run(host="localhost",debug=True)