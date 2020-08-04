import discord
from discord.ext import commands
import random


class Joker(commands.Cog):
    def __init__(self,bot,config):
        self.bot=bot
        self.config=config
        self.jokes=config["jokelist"]
        self.usedjokes=[]
    @commands.command()
    async def joke(self,ctx,*args):
        joke=random.choice(self.jokes)
        self.jokes.remove(joke)
        self.usedjokes.append(joke)
        if len(self.jokes)==0:
            self.jokes=self.usedjokes
            self.usedjokes=[]
        await ctx.send(joke)

cogs=[Joker]
