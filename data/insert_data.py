def get_database():
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://benclark1110:pokemonapi@cluster0.z17f56o.mongodb.net/pokemonDatabase"
    

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['pokemonDatabase']
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()

    collection_name = dbname["pokemonCollection"]

# import pymongo

# client = pymongo.MongoClient("mongodb+srv://benclark1110:pokemonapi@cluster0.z17f56o.mongodb.net/?retryWrites=true&w=majority")
# db = client.test

# print('called')