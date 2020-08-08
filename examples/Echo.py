#imports the required packages
from discord.ext import commands
import discord

#makes a cog where all of the commands and listeners will go
class Echo(commands.Cog):
    #defines bot to make it easier to write
    def __init__(self,bot,config=None):
         self.bot = bot
    #adds a command
    @commands.command()
    async def echo(self,ctx,*,message):
        """Echoes back whatever you say"""
        await ctx.send(message)
#tells EasyPluginBot that the cog Echo exists
cogs=[Echo]