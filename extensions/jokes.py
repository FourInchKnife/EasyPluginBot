import discord
from discord.ext import commands
import random


class Joker(commands.Cog):
    def __init__(self,bot,config):
        self.bot=bot
        self.config=config
        self.jokes=config["ext"]["Jokes"]["jokelist"]
    @commands.command()
    async def joke(self,ctx,*args):
        await ctx.send(random.choice(self.jokes));

cogs=[Joker]
