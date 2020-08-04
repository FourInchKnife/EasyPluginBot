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
    async def joke(self,ctx):
        """Tells a funny joke"""
        joke=random.choice(self.jokes)
        self.jokes.remove(joke)
        self.usedjokes.append(joke)
        if len(self.jokes)==0:
            self.jokes=self.usedjokes
            self.usedjokes=[]
        await ctx.send(joke)
    @commands.command()
    async def compare(self,ctx,first,second):
        """Compares any two values"""
        await ctx.send(first+" is better than "+second)

cogs=[Joker]
