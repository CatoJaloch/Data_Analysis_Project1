#connecting to an API with py
import requests
base_url = "https://pokeapi.co/api/v2/"  #base url for the pokeapi, we will use this to make requests to the API

def get_pokemon_info(name): #function to get pokemon info by name
    url = f"{base_url}pokemon/{name}"
    response = requests .get(url) #making a get request to the url to get the pokemon data
    print(response)  #this will print the response object, which contains the status code and the data from the api in json format
     #200 means success,404 means not found,401 means unauthorized,500 means server error
    if response.status_code== 200:
        pokemon_data = response.json() #pokimon data is in json format,convert it to a python dictionary using the json() method
        return pokemon_data 
    else:
        print(f"Failed to retrieve data {response.status_code}")    
pokemon_name = "typhlosion" #you can change the name to any pokemon you want to get info about
pokemon_info = get_pokemon_info(pokemon_name)   # this will call the function to get the pokemon info and stare the data in the pokemon_info variable
if pokemon_info: #if the pokemon_info variable
    print(f"{pokemon_info["name"]}")
    print(f"ID: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")
else:
    print(f"Failed to retrieve data for {pokemon_name}")