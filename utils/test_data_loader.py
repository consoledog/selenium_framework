import json

def load_test_data(file_path):
    with open(file_path) as file:
        return json.load(file)