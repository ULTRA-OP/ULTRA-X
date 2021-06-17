# COPYRIGHT © 2021-22 BY LEGENDX22

from .import db
x = db["alive"]

IMG = "https://telegra.ph/file/6f690f49b710d70859f44.jpg"
TEXT = '''
**
𝑼𝒍𝒕𝒓𝒂𝑿 2.0 𝒊𝒔 𝑶𝒏𝒍𝒊𝒏𝒆
𝑭𝒖𝒍𝒍𝒚 𝑺𝒆𝒄𝒖𝒓𝒆𝒅
𝑩𝒆𝒔𝒕 𝑴𝒐𝒅𝒖𝒍𝒆𝒔 𝑰𝒏𝒔𝒕𝒂𝒍𝒍𝒆𝒅
𝑼𝒔𝒆𝒓-𝑭𝒓𝒊𝒆𝒏𝒅𝒍𝒚
𝑭𝒖𝒍𝒍𝒚 𝑼𝒑𝒅𝒂𝒕𝒆𝒅 𝑼𝒔𝒆𝒓𝑩𝒐𝒕
**
'''

async def add_img(img):
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


async def pm_img(img):
  k = await x.find_one({'_id': "UltraX"})
  if k:
    await x.update_one({"_id": "UltraX"}, {"$set": {"img": img}})
  else:
    await x.insert_one({"_id": "UltraX", "img": img})

async def get_pm_img():
  X=await x.find_one({"_id": "UltraX"})
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
  k = await x.find_one({'_id': "ULTRA"})
  if k:
    await x.update_one({"_id": "ULTRA"}, {"$set": {"text": msg}})
  else:
    await x.insert_one({"_id": "ULTRA", "text": msg})

async def get_text():
  X=await x.find_one({"_id": "ULTRA"})
  if X:
    return X["text"]
  else:
    return TEXT

async def pm_text(msg):
  k = await x.find_one({'_id': "LEGENDXISBEST"})
  if k:
    await x.update_one({"_id": "LEGENDXISBEST"}, {"$set": {"text": msg}})
  else:
    await x.insert_one({"_id": "LEGENDXISBEST", "text": msg})

async def get_pm_text():
  X=await x.find_one({"_id": "LEGENDXISBEST"})
  if X:
    return X["text"]
  else:
    return False
