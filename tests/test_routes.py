import json
# from app.models import User
from conftest import fake

def test_new_user(client, init_database):
    """
    GIVEN the test user dict
    WHEN a new user is created
    THEN check that the username & email fields are defined correctly
    """
    test_user = {
        "name":fake.name(),
        "username":fake.username(),
        "company":fake.company(),
        "jobtitle":fake.jobtitle(),
        "email":fake.email(),
        "password":fake.password()
    }

    response = client.post(
        "/register", data=json.dumps(test_user), content_type="application/json"
    )
    data = response.json.get("user")
    assert response.status_code == 201
    assert data.get("email") == test_user.get("email")
    assert data.get("username") == test_user.get("username")

def test_login(client, init_database):
    user = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "username": fake.user_name(),
        "email": fake.email(),
        "bio": fake.text(),
        "password": fake.password(),
    }

    response = client.post(
        "/register", data=json.dumps(user), content_type="application/json"
    )

    assert response.status_code == 201

    response = client.post(
        "/login",
        data=json.dumps(
            {
                "email": user["email"],
                "password": user["password"],
            }
        ),
        content_type="application/json",
    )

    assert response.status_code == 200
    assert response.json["message"] == "You are logged in "



