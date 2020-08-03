from discord.ext import commands
import discord

class Echo(commands.Cog):
    def __init__(self,bot):
         self.bot = bot
    @commands.command()
    async def echo(self,ctx,*,message):
        """Replies with the message you send"""
        await ctx.send(message)
cogs=[Echo]
