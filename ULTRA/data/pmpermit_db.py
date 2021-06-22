# COPYRIGHT © 2021-22 BY LEGENDX22

from . import db
x = db["PMPERMIT_DATABASE"]

async def approve(id):
  k = await x.find_one({"_id": "LEGENDX"})
  if k:
    await x.update_one({"_id": "LEGENDX"}, {"$push": {"pm": id}})
  else:
    id = [id]
    await x.insert_one({"_id": "LEGENDX", "pm": id})

async def disapprove(id):
  await x.update_one({"_id": "LEGENDX"}, {"$pull": {"pm": id}})


async def is_approved(id):
  pro = await x.find_one({"_id": "LEGENDX"})
  if pro:
    X = list(pro.get("pm"))
    if id in X:
      return True
    else:
      return False
  else:
    return False

async def approved_list():
  k = await x.find_one({'_id': "LEGENDX"})
  if k:
    return list(k.get("pm"))
  else:
    return False
    
