from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

def get_database():
    # from pymongo import MongoClient
    # import pymongo

    CONNECTION_STRING = "mongodb+srv://benclark1110:pokemonapi@cluster0.z17f56o.mongodb.net/?retryWrites=true&w=majority"
    
    # from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    return client['pokemonDatabase']

dbname = get_database()

collection_name = dbname["pokemonCollection"]

charmnder_data = {
    "_id": 3,
    "name": "charmnder",
    "type": "fire",
    "caught": True
}

# class Pokemon:
#     _id: int
#     snamelug: str
#     type: str
#     caught: bool

#     def to_json(self):
#         return jsonify(self, exclude_none=True)

class Pokemon():

    def __init__(self, _id, name, type, caught):
        self._id = _id
        self.name = name
        self.type = type
        self.caught = caught


@app.route("/")
def get_all_pokemon():
    all_pokemon = collection_name.find()
    return jsonify([pokemon for pokemon in all_pokemon])

@app.route("/get_by_id/<int:_id>", methods=["GET"])
def find_one(_id):
    pokemon = collection_name.find({"_id": _id})
    return jsonify([pokemon for pokemon in pokemon])

@app.route("/add_pokemon", methods=["PUT", "POST"])
def add_pokemon():
    print(request.get_json())

    raw_pokemon = request.get_json()
    print(raw_pokemon["name"])
    # pokemon = Pokemon(raw_pokemon["_id"], raw_pokemon["name"], raw_pokemon["type"], raw_pokemon["caught"])
    # collection_name.insert_one(pokemon)
    return 'added'



@app.errorhandler(404)
def resource_not_found(e):
    """
    An error-handler to ensure that 404 errors are returned as JSON.
    """
    return jsonify(error=str(e)), 404


@app.errorhandler(400)
def resource_not_found(e):
    """
    An error-handler to ensure that MongoDB duplicate key errors are returned as JSON.
    """
    return jsonify(error=str(e)), 400