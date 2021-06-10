# COPYRIGHT © 2021-22 BY LEGENDX22
from . import db
x = db["PERSONAL_DATA"]
async def add_data(data):
  k = await x.find_one({"_id": "LEGENDX"})
  if k:
    await x.update_one({"_id": "LEGENDX"}, {"$push": {"data": data}})
  else:
    data = [data]
    await x.insert_one({"_id": "LEGENDX", "data": data})

async def rm_data(data):
  await x.update_one({"_id": "LEGENDX"}, {"$pull": {"data": data}})
async def already_data(data):
  pro = await x.find_one({"_id": "LEGENDX"})
  if pro:
    X = list(pro["data"])
    if data in X:
      return True
    else:
      return False
  else:
    return False

async def all_data():
  k = await x.find_one({'_id': "LEGENDX"})
  if k:
    return list(k["data"])
  else:
    return False
    
