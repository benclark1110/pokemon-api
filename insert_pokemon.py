import json, connection, model

pokemon_collection = connection.get_database()

with open('./pokemon.json') as file:
    pokemon_data = json.load(file)

modeled_pokemon = []

for pokemon in pokemon_data:
    pokemon = model.Pokemon(pokemon["_id"], pokemon["name"], pokemon["type"], pokemon["caught"])
    modeled_pokemon.append(pokemon.__dict__)

pokemon_collection.insert_many(modeled_pokemon) 