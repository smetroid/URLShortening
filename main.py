from flask import Flask
import shortuuid
URLShorteningAPI = Flask(__name__)

# Creating a dictionary to keep track of the data
UID_LIST = {}

@URLShorteningAPI.route("/encode")
def encode(url):
    # Check to make sure key does not already exists
    id = shortuuid.ShortUUID().random(length=6)
    url_short=id
    original_url=url
    URL_LIST[id] = original_url

    return "<p>encoded url</p>"
    #return encoded(url)

@URLShorteningAPI.route("/decode")
def decode(shortURL):
    original_url = UID_LIST[shortURL]
    return "<p>decoded url</p>"
    #return decode(url)