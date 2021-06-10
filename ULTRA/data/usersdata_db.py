# COPYRIGHT © 2021-22 BY LEGENDX22
from . import db
x = db["PERSONAL_DATA"]
async def add_data(data):
  await x.insert_one({"data": data})
async def remove_data(data):
  await x.delete_one({"data": data})
async def show_data():
  X = [fuck async for fuck in x.find()]
  return X
