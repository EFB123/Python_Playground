import requests
import json

class User:
    def __init__ (self, first_name: dict) -> None: 
        self.first_name = first_name

    def __str__ (self):
        return self.first_name

user_list : list[User]

def create_random_user():
    response = requests.get("https://randomuser.me/api/")
    results = json.loads(response.text)["results"][0]
    first_name = results["name"]["first"]
    return User(first_name)

print(create_random_user())