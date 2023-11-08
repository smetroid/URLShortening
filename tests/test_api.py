import pytest
from shorturl import shorturl
import json

# test data and defaults
JSON_DATA = '{ "url": "https://www.yahoo.com/news/dog-adopted-7-years-pennsylvania-210548824.html" }'
DATA = json.loads(JSON_DATA)
CONTENT_TYPE ="application/json"

@pytest.fixture()
def client():
    client = shorturl.test_client()
    yield client
    
#@pytest.fixture()
#def runner(app):
#    return app.test_cli_runner()

def test_encode(client):
    #assert client.get('/encode', data=None, content_type=CONTENT_TYPE).status_code == 200
    encoded_data = client.post('/encode', data=JSON_DATA, content_type=CONTENT_TYPE)
    id = json.loads(encoded_data.data)['id']
    #assert b'id' in response.data
    #assert b'short_url' in response.data
    #assert b'original_url' in response.data
    decode_test = '{"id":"'+id+'"}'
    decoded_data = client.post('/decode', data=decode_test, content_type=CONTENT_TYPE)
    origin_url = json.loads(decoded_data.data)['original_url']
    assert origin_url == DATA['url']
    #decoded_url = client('/decode', data=DATA, content_type=CONTENT_TYPE)
    #assert response.headers["Location"] == "/auth/login"

#def test_decode(client):
#    assert client.get('/decode').status_code == 200
#    assert client.post('/decode')

