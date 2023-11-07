from flask import Flask, request, jsonify
import shortuuid
shorturl = Flask(__name__)

# Creating a dictionary to keep track of the data
URL_LIST = {}

@shorturl.route("/")
def root():
    return "<p>this is root</p>"

@shorturl.route("/encode", methods=["POST"])
def encode():
    """generate a shortened url

    Returns:
        json: a serializable json object with a shortkey
    """
    try:
        if request.form['url']:
            id = shortuuid.ShortUUID().random(length=6)
            url = request.form['url']
            URL_LIST[id] = url
        return jsonify({id:url})
    except Exception as e:
        return e

@shorturl.route("/decode")
def decode():
    original_url = UID_LIST[shortURL]
    return "<p>decoded url</p>"
    #return decode(url)

# Needed for VSCode debugger
if __name__ == '__main__':
    shorturl.run(use_debugger=False, use_reloader=False, passthrough_errors=True)