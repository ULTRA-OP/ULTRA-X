from os import system
from ULTRA import mongo
import motor.motor_asyncio
# switch to motor because it's asynchronous call
# https://gist.github.com/anand2312/840aeb3e98c3d7dbb3db8b757c1a7ace
database = motor.motor_asyncio.AsyncIOMotorClient(mongo)
db = database ["ULTRA_X"]
