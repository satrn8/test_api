from schemas.reqres import create, update_put, update_patch
from utils.sessions import reqres
from pytest_voluptuous import S
from resources.information import user


def test_create():
    response = reqres().post('/api/users', data=user)
    assert response.status_code == 201
    assert str(response.json()['name']) == user["name"]
    assert str(response.json()['job']) == user["job"]
    assert S(create) == response.json()


def test_update_put():
    response = reqres().put("/api/users/2", data=user)
    assert response.status_code == 200
    assert str(response.json()['name']) == user["name"]
    assert str(response.json()['job']) == user["job"]
    assert S(update_put) == response.json()


def test_single_use_not_found():
    response = reqres().get("/api/users/23")
    assert response.status_code == 404


def test_update_patch():
    response = reqres().patch("/api/users/2", data=user)
    assert response.status_code == 200
    assert str(response.json()['name']) == user["name"]
    assert str(response.json()['job']) == user["job"]
    assert S(update_patch) == response.json()


def test_delayed_response():
    response = reqres().get('/api/users?delay=3')
    assert response.status_code == 200

    