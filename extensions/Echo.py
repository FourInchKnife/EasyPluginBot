#imports the required packages
from discord.ext import commands
import discord

#makes a cog where all of the commands and listeners will go
class Echo(commands.Cog):
    #defines bot to make it easier to write
    def __init__(self,bot,config):
         self.bot = bot
         self.config=config["Echo"]
    #adds a command
    @commands.command()
    async def echo(self,ctx,*,message):
        """Replies with the message you send"""
        await ctx.send(message)
#tells EasyPluginBot that the cog Echo exists
cogs=[Echo]
