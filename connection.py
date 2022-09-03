from pymongo import MongoClient

def get_database():
    
    CONNECTION_STRING = "mongodb+srv://benclark1110:pokemonapi@cluster0.z17f56o.mongodb.net/?retryWrites=true&w=majority"
    
    client = MongoClient(CONNECTION_STRING)

    dbname = client['pokemonDatabase']

    return dbname["pokemonCollection"]