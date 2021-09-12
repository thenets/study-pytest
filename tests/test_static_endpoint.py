import pytest


@pytest.mark.get
def test_static_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


@pytest.mark.get
def test_static_contact(client):
    response = client.get("/contact")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hi, I'm Luiz. You can reach me at https://thenets.org"
    }
