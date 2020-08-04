import discord
from discord.ext import commands
import requests as re
import json
'''
This extensions uses the Merriam-Webster dictionary api.
To actually use this you need to place your api keys in the
config.json file in the following format:

{
    "ext":{
        "MerriamWebster":{
            "learner":"learner key here",
            "dictionary":"dictionary key here"
        }
    }
}

You can get your keys by making an account at https://dictionaryapi.com/
'''

class merriamutils:
    def getdef(word):
         return json.loads(re.get("https://www.dictionaryapi.com/api/v3/references/learners/json/dragon?key=4c5a103b-53aa-4459-a276-c90b692f7633")._content)

class MerriamWebster(commands.Cog):
    '''In dev now...'''
    def __init__(self,bot,config):
        self.bot = bot
        self.config = config
    @commands.command()
    async def define(self,ctx,word):


cogs=[]
