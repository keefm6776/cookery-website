import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "cookbook"
COLLECTION_NAME = "recipes"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo has connected successfully!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Unable to connect to MongoDB: %s") % e
       
conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

documents = coll.find()

for doc in documents:
    print(doc)
    
    
    
