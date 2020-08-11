import discord
from discord.ext import commands
import datetime
import random

if __name__ == '__main__':
    print("Warn: this file is not meant to be run by the user.")

class ToDo(commands.Cog):
    def __init__(self,bot,config=None,keys=None):
        self.bot=bot
    async def getLists(self,ctx):
        IDs={}
        pins = await ctx.channel.pins()
        for i in pins:
            if i.author == ctx.guild.me:
                try:
                    IDs[(i.embeds[0].footer.text)]=i
                except:
                    pass
        return IDs
    async def getList(self,ctx,ID):
        lists = await self.getLists(ctx)
        return lists[ID]
    async def newID(self, ctx):
        todos=await self.getLists(ctx)
        while 1:
            testID=random.choice(alph)+random.choice(alph)+random.choice(alph)+random.choice(alph)+random.choice(alph)+random.choice(alph)
            try:
                todos[testID]
            except:
                return testID

    @commands.command()
    async def tdcreate(self,ctx,name,*,desc=''):
        embed=discord.Embed(title=name,description=desc)
        ID = await self.newID(ctx)
        embed.set_footer(text=ID)
        message = await ctx.send(None,embed=embed)
        await message.pin(reason="This message is a ToDo list")
    @commands.command()
    async def tdedit(self,ctx,listID,operation,*,value):
        operations=[]
        if not operation in operations:
            await ctx.send("`{}` is not a valid operation".format(operation))
            return
        if ':' in listID:
            list = (await getList(listID.split(':')[0]), listID.split(':')[1])

        else:
            list = (await getList(listID),None)


cogs=[ToDo]
