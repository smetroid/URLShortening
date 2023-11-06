from flask import Flask
URLShorteningAPI = Flask(__name__)

@URLShorteningAPI.route("/")
def encode():
    return "<p>encoded url</p>"
    #return encoded(url)

def decode():
    return "<p>decoded url</p>"
    #return decode(url)