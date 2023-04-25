import requests
import json

response = requests.get("https://randomuser.me/api/")

class Information:
    def __init__ (self, all_info : dict) -> None: 
        self.all_info = all_info

local_info_list : list[Information] #vår lokala info-lista

class Specific_info(Information):
    def __init__(self, all_info : dict, str_leaf : str):
        super().__init__(all_info)
        self.str_leaf = str_leaf

def move_info_from_web_to_local(key : str):
    ##### FINISH THIS #########
    # Använd "key" innuti response.text.data
    # Add as informion to local list



data = response.text #get data in json form
parse_json = json.loads(data) #make it to python object
print(type(parse_json)) #This is Dict = {}
print(type(parse_json["results"])) #This is List = []
print(type(parse_json["results"][0]))
relevant_info = (parse_json["results"])[0] #find relevant info 
#print(data)
print((relevant_info["name"])["title"])