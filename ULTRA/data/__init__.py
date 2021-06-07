from os import system
from ULTRA import mongo
import motor.motor_asyncio
# switch to motor because it's asynchronous call
database = mongo_client = motor.motor_asyncio.AsyncIOMotorClient(mongo)
db = database ["ULTRA_X"]
