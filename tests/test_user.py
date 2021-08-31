import pytest


@pytest.mark.post
@pytest.mark.parametrize(
    "username, password, expected_value, expected_bool",
    [
        ("zezinho", "xuxa", {"username": "zezinho", "password": "xuxa"}, True),
        ("kratos", "freya", {"username": "kratos", "password": "freya"}, True),
        ("admin", "admin", {"username": "admin", "password": "xuxa"}, False),
    ],
)
def test_user_create(client, username, password, expected_value, expected_bool):
    response = client.post("/user/", json={"username": username, "password": password})
    assert response.status_code == 200
    assert (response.json() == expected_value) == expected_bool
