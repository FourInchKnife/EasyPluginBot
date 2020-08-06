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
                "learner":"learner key here"
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
        if not self.key:
            self.key = input("Key for Merriam-Webster Learner's dictionary:")
    @commands.command()
    async def define(self,ctx,word):
        data = json.loads(re.get("https://www.dictionaryapi.com/api/v3/references/learners/json/{}?key={}".format(word,self.key))._content)
        embed=discord.Embed(title="Definition of {}".format(word))
        try:
            for i in data:
                if word in i["meta"]["app-shortdef"]["hw"]:
                    header = "{} [{}]".format(i["meta"]["app-shortdef"]["hw"],i["meta"]["app-shortdef"]["fl"])
                    body=""
                    for k in i["meta"]["app-shortdef"]["def"]:
                        q=k
                        formatting={"{it}":"*","{/it}":"*","{b}":"**","{/b}":"**","{bc}":"_ _\n•","{ldquo}":"“","{rdquo}":"”"}
                        for i in formatting:
                            q = q.replace(i, formatting[i])
                        body+=q+"\n"
                    embed.add_field(name=header,value=body,inline =False)
            await ctx.send(embed=embed)
        except TypeError as e:
            embed.add_field(name="No definitions found. Maybe try one of these words?",value="•"+"\n•".join(data))
            await ctx.send(embed=embed)

cogs=[MerriamWebster]
