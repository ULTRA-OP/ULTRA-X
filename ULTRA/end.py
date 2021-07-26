# COPYRIGHT © 2021-22 BY LEGENDX22
import os
def Var(var):
  pro = os.environ.get(var, None)
  return pro
def setVar(var, value):
  pro = os.environ[var] = value

string = Var("STRING_SESSION")
heroku_api = Var("HEROKU_API_KEY")
setVar("HEROKU_API_KEY", "Api secured by UltraX")
setVar("STRING_SESSION", "SESSION SECURED BY UltraX")

