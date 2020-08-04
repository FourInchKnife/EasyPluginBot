import discord
from discord.ext import commands
import random


class Joker(commands.Cog):
    def __init__(self,bot,config):
        self.bot=bot
        self.config=config
        self.jokes=config["ext"]["Jokes"]["jokelist"]
        self.blacklist=[]
        self.blacklistlength=config["ext"]["Jokes"]["blacklistlength"]
    @commands.command()
    async def joke(self,ctx,*args):
        jokes=[i for i in self.jokes if not i in self.blacklist]
        joke=random.choice(jokes)
        self.blacklist.append(joke)
        if len(self.blacklist)>3:
            self.blacklist.pop(0)
        await ctx.send(joke)

cogs=[Joker]
