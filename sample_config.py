import os

class Config(object):
  API_ID = os.environ.get("API_ID", None)  
  API_HASH = os.environ.get("API_HASH", None) 
  BOT_TOKEN = os.environ.get("BOT_TOKEN", None) 
  MONGO_URL = os.environ.get("MONGO_URL", None)
  DATABASE_NAME = os.environ.get("DATABASE_NAME") 
  BOT_USERNAME = os.environ.get("BOT_USERNAME") 
  UPDATE_CHNL = os.environ.get("UPDATE_CHNL")
  OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
  SUPPORT_GRP = os.environ.get("SUPPORT_GRP")
  BOT_NAME = os.environ.get("BOT_NAME")
  ADMINS = os.environ.get("ADMINS")
  START_IMG1 = os.environ.get("START_IMG1")
  START_IMG2 = os.environ.get("START_IMG2", None)
  START_IMG3 = os.environ.get("START_IMG3", None)
  START_IMG4 = os.environ.get("START_IMG4", None)
  START_IMG5 = os.environ.get("START_IMG5", None)
  START_IMG6 = os.environ.get("START_IMG6", None)
  START_IMG7 = os.environ.get("START_IMG7", None)
  START_IMG8 = os.environ.get("START_IMG8", None)
  START_IMG9 = os.environ.get("START_IMG9", None)
  START_IMG10 = os.environ.get("START_IMG10", None)
  STKR = os.environ.get("STKR")
  STKR1 = os.environ.get("STKR1", None)
  STKR2 = os.environ.get("STKR2", None)
  STKR3 = os.environ.get("STKR3", None)
  STKR4 = os.environ.get("STKR4", None)
  STKR5 = os.environ.get("STKR5", None)
  STKR6 = os.environ.get("STKR6", None)
  STKR7 = os.environ.get("STKR7", None)
  STKR8 = os.environ.get("STKR8", None)
  STKR9 = os.environ.get("STKR9", None)
  
