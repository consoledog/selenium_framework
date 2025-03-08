import pytest
from utils.api_client import APIClient

def test_get_users():
    users = APIClient.get_users()
    assert len(users) > 0  # Ensure API returns users

def test_create_user():
    new_user = {"name": "John Doe", "email": "john@example.com"}
    response = APIClient.create_user(new_user)
    assert response["name"] == new_user["name"]
    assert response["email"] == new_user["email"]
