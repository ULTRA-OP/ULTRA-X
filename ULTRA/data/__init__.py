from os import system
try:
  import pymongo
except:
  system("pip install pymongo && pip install dnspython")
from ULTRA import mongo
from pymongo import MongoClient as mg
database = mg(mongo)
db = database ["ULTRA_X"]
