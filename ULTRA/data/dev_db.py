# COPYRIGHT © 2021-22 BY LEGENDX22
from . import db
x = db["DEV"]

async def add_dev():
  X = await x.find_one({"_id": "LEGENDX"})
  if X:
    await x.update_one({"_id": "LEGENDX"}, {"$set": {"dev": "True"}})
  else:
    await x.insert_one({"_id": "LEGENDX", "dev": "True"})
async def rm_dev():
  await x.update_one({"_id": "LEGENDX"}, {"$set": {"dev": "False"}})

async def check_dev():
  X = await x.find_one({"_id": "LEGENDX"})
  if X:
    return X["dev"]
  else:
    return "False"
