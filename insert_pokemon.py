import json
import connection

pokemon_collection = connection.get_database()

with open('./pokemon.json') as file:
    pokemon_data = json.load(file)

pokemon_collection.insert_many(pokemon_data) 