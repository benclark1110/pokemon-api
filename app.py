from flask import Flask, request, jsonify
import connection
import model

app = Flask(__name__)

pokemon_collection = connection.get_database()

@app.route("/")
def get_all_pokemon():
    all_pokemon = pokemon_collection.find()
    return jsonify([pokemon for pokemon in all_pokemon])

@app.route("/get_by_id/<int:_id>", methods=["GET"])
def find_one_pokemon(_id: int):
    pokemon = pokemon_collection.find({"_id": _id})
    return jsonify([pokemon for pokemon in pokemon])

@app.route("/add_pokemon", methods=["PUT", "POST"])
def add_pokemon():
    raw_pokemon = request.get_json()
    pokemon = model.Pokemon(raw_pokemon["_id"], raw_pokemon["name"], raw_pokemon["type"], raw_pokemon["caught"])
    pokemon_collection.insert_one(pokemon.__dict__)
    return 'added'

@app.route("/filter_by_type/<string:type>", methods=["GET"])
def filter_by_type(type: str):
    pokemon = pokemon_collection.find({"type": type})
    return jsonify([pokemon for pokemon in pokemon])

@app.route("/filter_by_name/<string:name>", methods=["GET"])
def filter_by_name(name: str):
    pokemon = pokemon_collection.find({"name": name})
    return jsonify([pokemon for pokemon in pokemon])

@app.route("/get_pokemon_caught", methods=["GET"])
def get_pokemon_caught():
    pokemon = pokemon_collection.find({"caught": True})
    return jsonify([pokemon for pokemon in pokemon])

@app.route("/get_pokemon_not_caught", methods=["GET"])
def get_pokemon_not_caught():
    pokemon = pokemon_collection.find({"caught": False})
    return jsonify([pokemon for pokemon in pokemon])

@app.route("/mark_as_caught/<string:name>", methods=["PUT", "POST"])
def mark_as_caught(name: str):
    pokemon_collection.find_one_and_update({'name': name}, {"$set": {'caught': True}})
    return 'Pokemon Caught!'

@app.route("/mark_as_released/<string:name>", methods=["PUT", "POST"])
def mark_as_released(name: str):
    pokemon_collection.find_one_and_update({'name': name}, {"$set": {'caught': False}})
    return 'Pokemon Released'

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