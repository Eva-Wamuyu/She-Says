from fastapi.testclient import TestClient
from fastapi import HTTPException
from . import models
from .app import app

client = TestClient(app)



def test_index():
    response = client.get("/")
    assert response.json() ==  {
        "message": "Go to /docs for more information"
    }
