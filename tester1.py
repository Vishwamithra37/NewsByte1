from config import *
from dbconfig import *
import hashlib
import datetime


def get_hash(input_string,trunc_length=6):
    hash_url=hashlib.md5(input_string.encode()).hexdigest()[:trunc_length]
    hash_url=SECURITY+RUNNINGDOMAIN+":"+str(RUNNINGPORT)+"/"+hash_url
    return hash_url

@app.route('/api/compressor',methods=['POST'])
def direct():
    """
     ---
    post:
      description: Returns the compressed/hashed URL.
      parameters:
        - name: url
          in: body
          required: true
          description: Give the URL to be compressed.
          schema:
            type : JSON
            required:
              - url
            properties:
                url:
                    type: string
                    description: Give the URL to be compressed.
                    example: https://www.google.com/currypuff?q=aloo&p=isittasty
      responses:
        200:
          description: Returns JSON with short_url.
          content:
            application/json:
              schema: post_response
              example: {"short_url": "https://mydomain/8ffdef"}
        500:
          description: The URL given has an escape character.

    """


    dat= flask.request.get_json()
    url = dat['url']
    assert len(url.split('\\'))==1

    hash_url=get_hash(url)
    checking=dac.find_one({"short_url":hash_url})

    if checking is None:
        dac.insert_one({"org_url":url,"short_url":hash_url,"created_at":datetime.datetime.utcnow()})
        return flask.jsonify({"short_url":hash_url})
    elif checking["org_url"]!=url:
                    hash_url=get_hash(url,trunc_length=5)
                    dac.insert_one({"org_url":url,"short_url":hash_url,"created_at":datetime.datetime.utcnow()})
                    return flask.jsonify({"short_url":hash_url})
    return flask.jsonify({"short_url":checking['short_url']})    


docs.register(target=direct)


@app.route('/<shorturl>',methods=['GET'])
def redirect(shorturl):
    """
     ---
    get:
      description: Returns the compressed/hashed URL.
      parameters:
        - name: url
          in: path
          required: true
          description: Give the URL to be compressed.
          schema:
            type : string
            required:
              - url
            properties:
                url:
                    type: string
                    description: Give the URL to be compressed.
                    example: "https://mydomain/8ffdef"
      responses:
        200:
          description: Redirects to the expected URL.
          content:
            redirect:
              schema: post_response
              example: "https://www.google.com/currypuff?q=aloo&p=isittasty"
        404:
            description: The URL given is not found.     
    """


    shorturl=SECURITY+RUNNINGDOMAIN+":"+str(RUNNINGPORT)+"/"+shorturl
    checking=dac.find_one({"short_url":shorturl})

    if checking is None:
        return "<h1>URL not found :<h1/>",404
    else:
        # Return to url checking["org_url"]
        return flask.redirect(checking['org_url'])
        
docs.register(target=redirect)


if __name__ == '__main__':
    app.run(host=RUNNINGDOMAIN,port=RUNNINGPORT,debug=True)