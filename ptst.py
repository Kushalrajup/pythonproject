import pytest
import json
import requests

def test_login():
    url="https://reqres.in/api/login/"
    data={'email':'eve.holt@reqres.in','password':'cityslicka'}
    response=requests.post(url,data=data)
    token=json.loads(response.text)
    assert response.status_code==200
