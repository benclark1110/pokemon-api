def get_database():
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://benclark1110:pokemonapi@cluster0.z17f56o.mongodb.net/?retryWrites=true&w=majority"
    
    print('called1')


    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['pokemonDatabase']
    
# This is added so that many files can reuse the function get_database()
# if __name__ == "__main__":    
    
    # Get the database
dbname = get_database()
print(dbname)

collection_name = dbname["pokemonCollection"]
print(collection_name)

item_1 = {
    "_id": 1,
    "name": "pikachu",
    "type": "electric",
    "caught": True
}

item_2 = {
    "_id": 2,
    "name": "squirtle",
    "type": "water",
    "caught": False
}

collection_name.insert_one(item_2)