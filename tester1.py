from traceback import print_tb
from config import *
from dbconfig import *
import hashlib

@app.route('/compressor',methods=['POST'])
def index():
    dat= flask.request.get_json()
    url = dat['url']
    assert len(url.split('\\'))==1
    hashurl=hashlib.sha224(url.encode('utf-8')).hexdigest()
    hashurl=hashurl[:6] # truncate to 6 chars.

    return "<h1>Welcome to NewsBytes_VishwaMithra</h1><br><br><h2>Please visit "+url
docs.register(target=index)


if __name__ == '__main__':
    app.run(host=RUNNINGDOMAIN,debug=True)