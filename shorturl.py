from flask import Flask, request, jsonify
import shortuuid
import json
shorturl = Flask(__name__)

# Creating a dictionary to keep track of the data
URL_LIST = {}

@shorturl.route("/")
def root():
    return "<p>this is root</p>"

@shorturl.route("/encode", methods=["POST", "GET"])
def encode():
    """generate a shortened url

    Returns:
        json: a serializable json object with a shortkey
    """
    try:
        data = request.data
        if type(data) is not str and data is not None:
            original_url = json.loads(data)
            id = shortuuid.ShortUUID().random(length=6)
            url = original_url['url']
            URL_LIST[id] = url

        return jsonify({id:url})

    except Exception as e:
        return jsonify(e.msg)


@shorturl.route("/decode", methods=["POST"])
def decode():
    """Decode a shorturl id into the original url passed before it was shortened

    Returns:
        json : the original url submitted, before the url shortening
    """
    try:
        if request.form['shorturl_id']:
            id = request.form['shorturl_id']

        return jsonify({URL_LIST[id]})

    except Exception as e:
        return json.dumps(e)

    # Needed for VSCode debugger
if __name__ == '__main__':
    shorturl.run(use_debugger=False, use_reloader=False, passthrough_errors=True)
