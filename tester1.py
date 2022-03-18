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
    hashurl=RUNNINGDOMAIN+'/'+hashurl[:6] # truncate to 6 chars
    checking=dac.find_one({"org_url":url})

    if checking is None:
        dac.insert_one({"org_url":url,"short_url":hashurl})
        return flask.jsonify({"short_url":hashurl})
    else:
        return flask.jsonify({"short_url":checking['short_url']})    
docs.register(target=index)


if __name__ == '__main__':
    app.run(host=RUNNINGDOMAIN,debug=True)