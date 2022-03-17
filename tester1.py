# from urllib import request
from config import *
#############################Initialized variables############################
utm_array=["utm_source","utm_medium","utm_campaign","utm_term","utm_content"]
#############################Initialized variables#############################

@app.route('/')
def index():
    # Get all args in the url.
    args = flask.request.args.to_dict()
    # Get the url.
    url = flask.request.url
    print(args)
    for i in utm_array:
        print(flask.request.args.get(i))
    return "Hello World!"+"<br>"+url    
docs.register(target=index)


if __name__ == '__main__':
    app.run(host="localhost",debug=True)