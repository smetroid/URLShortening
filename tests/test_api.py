import pytest
from shorturl import shorturl

@pytest.fixture()
def client():
    client = shorturl.test_client()
    yield client
    
#@pytest.fixture()
#def runner(app):
#    return app.test_cli_runner()

def test_encode(client):
    assert client.get('/encode').status_code == 200
    data = '{ "url": "https://www.yahoo.com/news/dog-adopted-7-years-pennsylvania-210548824.html" }'
    assert client.post('/encode', data=data, content_type='application/json').status_code == 200
    #assert response.headers["Location"] == "/auth/login"

