from flask import Flask, request, jsonify
import shortuuid
import json
from urllib.parse import urlparse
from flask_limiter import Limiter


shorturl = Flask(__name__)
limiter = Limiter(app=shorturl, key_func= lambda: 'global', default_limits=["2 per second"])

# Creating a dictionary to keep track of the data
URL_LIST = {}


def get_tld(url):
    """Get top level domain/information from url

    Args:
        url (string): url to parse

    Returns:
        string : top level information of an url ... eg: https://www.yahoo.com
    """
    parsed_url = urlparse(url)
    scheme = parsed_url.scheme
    hostname = parsed_url.hostname
    tld = scheme+"://"+hostname
    return tld


@shorturl.route("/encode", methods=["POST", "GET"])
def encode():
    """generate a shortened url

    Returns:
        json: a json object with an id, short url
    """
    try:
        if request.method == "POST":
            data = json.loads(request.data)
            id = shortuuid.ShortUUID().random(length=6)
            url = data['url']
            domain = get_tld(url)
            short_url = domain +"/" + id
            URL_LIST[id] = url
            return jsonify({"id":id,"short_url": short_url})

        if request.method == "GET":
            return jsonify({"message": "Get request succeeded"})

    # handling the GET request when no data is passed
    except json.JSONDecodeError as e:
            return jsonify({"message":"unable to parse request data ... please check documentation"})

    except Exception as e:
        return jsonify({"msg": "Exception"})


@shorturl.route("/decode", methods=["POST", "GET"])
def decode():
    """Decode a shorturl id into the original url passed before it was shortened

    Returns:
        json : the original url submitted, before the url shortening
    """
    try:
        data = request.data
        if type(data) is not str and len(data) > 0:
            shorturl_data = json.loads(data)
            id = shorturl_data['id']
        else:
            return jsonify({})

        return jsonify({"id":id,"original_url":URL_LIST[id]})

    except KeyError as e:
        return jsonify({"msg": "id submitted does not exist"})
    except Exception as e:
        return jsonify(e)

    # Needed for VSCode debugger
if __name__ == '__main__':
    shorturl.run(use_debugger=False, use_reloader=False, passthrough_errors=True)
