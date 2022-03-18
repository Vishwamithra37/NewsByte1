from traceback import print_tb
from config import *
from dbconfig import *

@app.route('/compressor',methods=['POST'])
def index():
    dat= flask.request.get_json()
    url = dat['url']
    assert len(url.split('\\'))==1
    





    return "<h1>Welcome to NewsBytes_VishwaMithra</h1><br><br><h2>Please visit "+url
docs.register(target=index)


if __name__ == '__main__':
    app.run(host=RUNNINGDOMAIN,debug=True)