# COPYRIGHT © 2021-22 BY LEGENDX22

from .import db
x = db["alive"]

IMG = "https://telegra.ph/file/e033d3f7ebcf8ce554ae5.jpg"
async def add_img(img=IMG):
  k = await x.find_one({'_id': "LEGENDX"})
  if k:
    await x.update_one({"_id": "LEGENDX"}, {"$set": {"img": img}}
  else:
    await x.insert_one({"_id": "LEGENDX", "img": img})

async def get_img():
  X=await x.find_one({"_id": "LEGENDX"})
  if X:
    return X["img"]
  else:
    return IMG
