import discord
from discord.ext import commands


class Joker(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    @commands.command()
    def joke(self,ctx,*args):
        pass
