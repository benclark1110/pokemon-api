import json
from pymongo import MongoClient
 
 
# Making Connection
myclient = MongoClient("mongodb://localhost:27017/")
  
# database
db = myclient["GFG"]
  
# Created or Switched to collection
# names: GeeksForGeeks
Collection = db["data"]
 
# Loading or Opening the json file
# with open('../pokemon.json') as file:
#     file_data = json.load(file)

file_data = {
    "_id": 1,
    "name": "pikachu",
    "type": "electric",
    "caught": True
}
     
# Inserting the loaded data in the Collection
# if JSON contains data more than one entry
# insert_many is used else insert_one is used
if isinstance(file_data, list):
    Collection.insert_one(file_data) 
    print('called1')
else:
    Collection.insert_one(file_data)
    print('called2')