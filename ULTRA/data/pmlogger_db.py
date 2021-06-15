# COPYRIGHT © 2021-22 BY LEGENDX22
from . import db
x = db["PM_LOGGER"]

async def add_logger():
  X = await x.find_one({"_id": "LEGENDX"})
  if X:
    await x.update_one({"_id": "LEGENDX"}, {"$set": {"logger": "True"}})
  else:
    await x.insert_one({"_id": "LEGENDX", "logger": "True"})
async def rm_logger():
  await x.update_one({"_id": "LEGENDX"}, {"$set": {"logger": "False"}})

async def check_logger():
  X = await x.find_one({"_id": "LEGENDX"})
  if X:
    return X["logger"]
  else:
    return "False"
