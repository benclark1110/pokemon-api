from flask import Flask, request, jsonify
import connection
import model

app = Flask(__name__)

collection_name = connection.get_database()

charmnder_data = {
    "_id": 3,
    "name": "charmnder",
    "type": "fire",
    "caught": True
}

@app.route("/")
def get_all_pokemon():
    all_pokemon = collection_name.find()
    return jsonify([pokemon for pokemon in all_pokemon])

@app.route("/get_by_id/<int:_id>", methods=["GET"])
def find_one_pokemon(_id):
    pokemon = collection_name.find({"_id": _id})
    return jsonify([pokemon for pokemon in pokemon])

@app.route("/add_pokemon", methods=["PUT", "POST"])
def add_pokemon():
    raw_pokemon = request.get_json()
    pokemon = model.Pokemon(raw_pokemon["_id"], raw_pokemon["name"], raw_pokemon["type"], raw_pokemon["caught"])
    collection_name.insert_one(pokemon.__dict__)
    return 'added'

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