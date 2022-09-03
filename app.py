from flask import Flask, request, jsonify
import connection, model, datetime

app = Flask(__name__)

pokemon_collection = connection.get_database()

@app.route("/", methods=["GET"])
def get_all_pokemon():
    """
    Returns all pokemon in Pokedex
    """
    all_pokemon = pokemon_collection.find()
    return jsonify([pokemon for pokemon in all_pokemon])

@app.route("/get_by_id/<int:_id>", methods=["GET"])
def find_one_pokemon(_id: int):
    """
    Returns one pokemon based on '_id'
    Parameters: _id(int)
    """
    pokemon = pokemon_collection.find({"_id": _id})
    return jsonify([pokemon for pokemon in pokemon])

@app.route("/add_pokemon", methods=["PUT", "POST"])
def add_pokemon():
    """
    Add a pokemon to the Pokedex
    {
        "name": "pokemonName",
        "type": "pokemonType",
        "caught": true/false,
        "_id": 99
    }
    """
    try: 
        raw_pokemon = request.get_json()
        pokemon = model.Pokemon(raw_pokemon["_id"], raw_pokemon["name"], raw_pokemon["type"], raw_pokemon["caught"])
        pokemon_collection.insert_one(pokemon.__dict__)
    except Exception as error:
        return jsonify(error=str(error))
    return 'Pokemon successfully added to Pokedex!'

@app.route("/filter_by_type/<string:type>", methods=["GET"])
def filter_by_type(type: str):
    """
    Returns pokemon filtered by type
    Parameters: type(string)
    """
    pokemon = pokemon_collection.find({"type": type})
    return jsonify([pokemon for pokemon in pokemon])

@app.route("/filter_by_name/<string:name>", methods=["GET"])
def filter_by_name(name: str):
    """
    Returns pokemon filtered by name
    Parameters: name(string)
    """
    pokemon = pokemon_collection.find({"name": name})
    return jsonify([pokemon for pokemon in pokemon])

@app.route("/get_caught_pokemon", methods=["GET"])
def get_caught_pokemon():
    """
    Returns all pokemon in Pokedex you have caught
    """
    pokemon = pokemon_collection.find({"caught": True})
    return jsonify([pokemon for pokemon in pokemon])

@app.route("/get_pokemon_not_caught", methods=["GET"])
def get_pokemon_not_caught():
    """
    Returns all pokemon in Pokedex you have not caught
    """
    pokemon = pokemon_collection.find({"caught": False})
    return jsonify([pokemon for pokemon in pokemon])

@app.route("/mark_as_caught/<string:name>", methods=["PUT", "POST"])
def mark_as_caught(name: str):
    """
    Marks a pokemon as caught
    Parameters: name(string)
    """
    pokemon_collection.find_one_and_update({'name': name}, {"$set": {'caught': True, 'lastUpdated': datetime.datetime.now()}})
    return f'You Caught a {name}!'

@app.route("/mark_as_released/<string:name>", methods=["PUT", "POST"])
def mark_as_released(name: str):
    """
    Marks a pokemon as released
    Parameters: name(string)
    """
    pokemon_collection.find_one_and_update({'name': name}, {"$set": {'caught': False, 'lastUpdated': datetime.datetime.now()}})
    return f'You Released a {name}.'

@app.errorhandler(404)
def resource_not_found(e):
    """
    Resource Not Found Error Handler
    """
    return jsonify(error=str(e)), 404

@app.errorhandler(400)
def bad_request(e):
    """
    Bad Request Error Handler
    """
    return jsonify(error=str(e)), 400

########### Pagination option ###########

@app.route("/pagination", methods=["GET"])
def get_some_pokemon():
    args = request.args
    skip = args.get('skip')
    limit = args.get('limit')

    if None not in (skip, limit):
        all_pokemon = pokemon_collection.find().skip(int(skip)).limit(int(limit))
    elif skip:
        all_pokemon = pokemon_collection.find().skip(int(skip))
    elif limit:
        all_pokemon = pokemon_collection.find().limit(int(limit))
    else:
        all_pokemon = pokemon_collection.find()

    return jsonify([pokemon for pokemon in all_pokemon])