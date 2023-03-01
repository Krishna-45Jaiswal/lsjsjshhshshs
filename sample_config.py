import os
from typing import Set

from telethon.tl.types import ChatBannedRights
from validators.url import url


class Config(object):
    API_ID = os.environ.get("API_ID", None) 
  
  
