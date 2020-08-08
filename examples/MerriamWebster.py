import discord
from discord.ext import commands
import requests as re
import json
from io import BytesIO

'''
This extensions uses the Merriam-Webster dictionary api.
To actually use this you need to place your api keys in the
keys.json file in the following format:

{
    "ext":{
        "MerriamWebster":{
            "MerriamWebster":"learner key here"
        }
    }
}

You can get your keys by making an account at https://dictionaryapi.com/
'''

class MerriamWebster(commands.Cog):
    def __init__(self,bot,config,key):
        self.bot = bot
        self.key=key
        if not self.key:
            self.key = input("Key for Merriam-Webster Learner's dictionary:")
    @commands.command()
    async def define(self,ctx,word):
        '''Uses Meriam-Webster\'s API to return a definition for a given word'''
        data = json.loads(re.get("https://www.dictionaryapi.com/api/v3/references/learners/json/{}?key={}".format(word,self.key))._content)
        embed=discord.Embed(title="Definition of {}".format(word))
        try:
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
        except Exception as e:
            outputFile=discord.File(BytesIO(json.dumps(data, sort_keys=True, indent=4).encode()),filename="output.json")
            await ctx.send("So that threw an error: ```{}```\nI'll attach all of the data I got.".format(e),file=outputFile)

cogs=[MerriamWebster]
