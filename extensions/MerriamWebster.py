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
            "MerriamWebster":{
                "learner":"learner key here",
                "dictionary":"dictionary key here"
            }
        }
    }
}

You can get your keys by making an account at https://dictionaryapi.com/
'''

class MerriamWebster(commands.Cog):
    '''In dev now...'''
    def __init__(self,bot,config):
        self.bot = bot
        self.key=config["learner"]
    @commands.command()
    async def define(self,ctx,word):
        data = json.loads(re.get("https://www.dictionaryapi.com/api/v3/references/learners/json/{}?key={}".format(word,self.key))._content)
        embed=discord.Embed(title="Definition of {}".format(word))
        for i in data:
            header = "{} [{}]".format(i["meta"]["app-shortdef"]["hw"],i["meta"]["app-shortdef"]["fl"])
            body=""
            for k in i["meta"]["app-shortdef"]["def"]:
                q="***".join(k.split("{b}{it}"))
                q="***".join(q.split("{/it}{/b}"))
                q="*".join(q.split("{it}"))
                q="*".join(q.split("{/it}"))
                q="**".join(q.split("{b}"))
                q="**".join(q.split("{b/}"))
                q="\n•".join(q.split("{bc}"))
                q="\"".join(q.split("{ldquo}"))
                q="\"".join(q.split("{rdquo}"))
                body+=q+"\n"
            embed.add_field(name=header,value=body)
        await ctx.send(embed=embed)

cogs=[MerriamWebster]
