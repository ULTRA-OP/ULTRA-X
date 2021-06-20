# COPYRIGHT © 2021-22 BY LEGENDX22

from . import db
x = db["sudolist"]

async def add_sudo(id):
  k = await x.find_one({"_id": "LEGENDX"})
  if k:
    await x.update_one({"_id": "LEGENDX"}, {"$push": {"sudo": id}})
  else:
    id = [id]
    await x.insert_one({"_id": "LEGENDX", "sudo": id})

async def rm_sudo(id):
  await x.update_one({"_id": "LEGENDX"}, {"$pull": {"sudo": id}})
async def is_sudo(id):
  pro = await x.find_one({"_id": "LEGENDX"})
  if pro:
    X = list(pro.get("sudo"))
    if id in X:
      return True
    else:
      return False
  else:
    return False

async def all_sudo():
  k = await x.find_one({'_id': "LEGENDX"})
  if k:
    return list(k.get("sudo"))
  else:
    return False
    
