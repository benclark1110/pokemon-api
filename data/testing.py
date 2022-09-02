import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:8080/")
mydb = myclient["mydatabase"]

mycol = mydb["customers"]

print(mydb.list_collection_names())
