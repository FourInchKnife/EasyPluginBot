import discord
from discord.ext import commands
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

class MerriamWebster(commands.Cog):
    '''Not yet implemented :('''
    def __init__(self,bot,config):
        self.bot = bot
        self.config = config

cogs=[]
