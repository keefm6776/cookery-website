import pymongo
import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["MONGO_DBNAME"] = 'cookbook'

#MONGODB_URI =   'mongodb+srv://root:31Wirpbj6677@cookery-website-xysxa.mongodb.net/cookbook?retryWrites=true&w=majority'
#DBS_NAME = "cookbook"
#COLLECTION_NAME = "recipes"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo has connected successfully!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Unable to connect to MongoDB: %s") % e
       
##conn = mongo_connect(MONGODB_URI)
##coll = conn[DBS_NAME][COLLECTION_NAME]

##documents = conn.find()

##for doc in documents:
  ##  print(doc)
    
    
    
