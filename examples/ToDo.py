import discord
from discord.ext import commands
import datetime
import random

class ToDo(commands.Cog):
    def __init__(self,bot,config=None,keys=None):
        self.bot=bot
    async def newID(self, ctx):
        alph=("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        IDs=[]
        pins = await ctx.channel.pins()
        for i in pins:
            if i.author == ctx.guild.me:
                try:
                    IDs.append(i.embeds[0].footer.text)
                except:
                    pass
        IDs.append("000000")
        testID="000000"
        while testID in IDs:
            testID=random.choice(alph)+random.choice(alph)+random.choice(alph)+random.choice(alph)+random.choice(alph)+random.choice(alph)
        return testID

    @commands.command()
    async def tdcreate(self,ctx,name,*,desc=''):
        embed=discord.Embed(title=name,description=desc)
        ID = await self.newID(ctx)
        embed.set_footer(text=ID)
        message = await ctx.send(None,embed=embed)
        await message.pin(reason="This message is a ToDo list")

cogs=[ToDo]
