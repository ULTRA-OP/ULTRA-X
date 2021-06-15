# COPYRIGHT © 2021-22 BY LEGENDX22

from .import db
x = db["alive"]

IMG = "https://telegra.ph/file/e033d3f7ebcf8ce554ae5.jpg"
async def add_img(img=IMG):
  k = await x.find_one({'_id': "LEGENDX"})
  if k:
    await x.update_one({"_id": "LEGENDX"}, {"$set": {"img": img}})
  else:
    await x.insert_one({"_id": "LEGENDX", "img": img})

async def get_img():
  X=await x.find_one({"_id": "LEGENDX"})
  if X:
    return X["img"]
  else:
    return IMG

async def add_token(token):
  k = await x.find_one({'_id': "LEGENDXOP"})
  if k:
    await x.update_one({"_id": "LEGENDXOP"}, {"$set": {"token": token}})
  else:
    await x.insert_one({"_id": "LEGENDXOP", "token": token})

async def get_token():
  X=await x.find_one({"_id": "LEGENDXOP"})
  if X:
    return X["token"]
  else:
    return False

async def add_grp(id):
  k = await x.find_one({'_id': "LEGENDX22"})
  if k:
    await x.update_one({"_id": "LEGENDX22"}, {"$set": {"group": id}})
  else:
    await x.insert_one({"_id": "LEGENDX22", "group": id})

async def get_grp():
  X=await x.find_one({"_id": "LEGENDX22"})
  if X:
    return X["group"]
  else:
    return False

async def add_text(msg):
  k = await x.find_one({'_id': "LEGENDXISBEST"})
  if k:
    await x.update_one({"_id": "LEGENDXISBEST"}, {"$set": {"text": msg}})
  else:
    await x.insert_one({"_id": "LEGENDXISBEST", "text": msg})

async def get_text():
  X=await x.find_one({"_id": "LEGENDXISBEST"})
  if X:
    return X["text"]
  else:
    return False
