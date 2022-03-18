from config import *
from dbconfig import *
import hashlib


def get_hash(input_string,trunc_length=6):
    hash_url=hashlib.md5(input_string.encode()).hexdigest()[:trunc_length]
    hash_url=SECURITY+RUNNINGDOMAIN+":"+str(RUNNINGPORT)+"/"+hash_url
    return hash_url

@app.route('/compressor',methods=['POST'])
def direct():
    dat= flask.request.get_json()
    url = dat['url']
    assert len(url.split('\\'))==1

    hash_url=get_hash(url)

    checking=dac.find_one({"short_url":hash_url})
    if checking["org_url"]==url:
        hash_url=get_hash(url,trunc_length=5)
        
    if checking is None:
        dac.insert_one({"org_url":url,"short_url":hash_url,"TTL":URL_LIFETIME})
        return flask.jsonify({"short_url":hash_url})
    else:
        return flask.jsonify({"short_url":checking['short_url']})    

docs.register(target=direct)

@app.route('/<shorturl>',methods=['GET'])
def redirect(shorturl):
    checking=dac.find_one({"short_url":shorturl})
    if checking is None:
        return "<h1>URL not found :<h1/>",404
    else:
        return flask.redirect(checking['org_url'])




if __name__ == '__main__':
    app.run(host=RUNNINGDOMAIN,port=RUNNINGPORT,debug=True)