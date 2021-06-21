# COPYRIGHT © 2021-22 BY LEGENDX22

from . import db
x = db["WAIFU_DATABASE"]

async def add_waifu(id):
  k = await x.find_one({"_id": "LEGENDX"})
  if k:
    await x.update_one({"_id": "LEGENDX"}, {"$push": {"wafu": id}})
  else:
    id = [id]
    await x.insert_one({"_id": "LEGENDX", "wafu": id})

async def rm_waifu(id):
  await x.update_one({"_id": "LEGENDX"}, {"$pull": {"wafu": id}})
async def is_waifu(id):
  pro = await x.find_one({"_id": "LEGENDX"})
  if pro:
    X = list(pro.get("wafu"))
    if id in X:
      return True
    else:
      return False
  else:
    return False

async def all_waifu():
  k = await x.find_one({'_id': "LEGENDX"})
  if k:
    return list(k.get("wafu"))
  else:
    return False
    
