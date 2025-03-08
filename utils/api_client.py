import requests

class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"  # Replace with API

    @staticmethod
    def get_users():
        response = requests.get(f"{APIClient.BASE_URL}/users")
        return response.json()

    @staticmethod
    def get_user(user_id):
        response = requests.get(f"{APIClient.BASE_URL}/users/{user_id}")
        return response.json()

    @staticmethod
    def create_user(data):
        response = requests.post(f"{APIClient.BASE_URL}/users", json=data)
        return response.json()
