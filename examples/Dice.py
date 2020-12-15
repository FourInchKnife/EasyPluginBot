from discord.ext import commands
import discord
from random import randint
import asyncio
import datetime

class Roll(commands.Cog):
    def __init__(self,bot,config,key):
        self.bot = bot
    def diceRoll(self,amount,type, stopat = None):
        rolls = []
        for i in range(amount):
            if stopat != None and datetime.datetime.now() > stopat:
                raise TimeoutError("That would take more than 3 seconds.")
            rolls.append(randint(1,type))
        return rolls
    @commands.command()
    async def roll(self,ctx, *, args):
        await self.rollDice(ctx,args,datetime.datetime.now() + datetime.timedelta(seconds = 3))
    async def quickSort(self,arr,stopat = None):
        less = []
        pivotList = []
        more = []
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            for i in arr:
                if stopat != None and datetime.datetime.now() > stopat:
                    raise TimeoutError("That would take more than 3 seconds.")
                if i < pivot:
                    less.append(i)
                elif i > pivot:
                    more.append(i)
                else:
                    pivotList.append(i)
            less = self.quickSort(less)
            more = self.quickSort(more)
            return more + less + pivotList
    async def rollDice(self, ctx, args, stopat):
        async with ctx.channel.typing():
            bits = args.split("!",1)
            data = bits[0]
            rolls = []
            keptRolls = []
            if len(bits) == 1:
                comment = None
            else:
                comment = bits[1]
            for i in "+-*/^":
                if i in data:
                    raise TypeError(\
                    """I'm not your personal calculator so I don't support `{0}`.
Do the math yourself.""".format(i))
            if data.count("d") != 1:
                raise TypeError(\
                """I need exactly one rolling statement.
Use the syntax `<x>d<y>` where `<x>` is the amount and `<y>` is the type.""")
            if data.count("k") > 1:
                raise TypeError(\
                """You can have a maximum of one keep statement per roll.
If you want a keep statement, use the syntax `k<a>` where `<a>` is the amount to keep.
To keep the lowest `<a>`, use `kl<a>`""")
            dataList = data.split(" ")
            for i in dataList:
                if "d" in i:
                    iSplit = i.split("d")
                    if len(iSplit) > 1:
                        rolls += self.diceRoll(int(iSplit[0]),int(iSplit[1]),stopat = stopat)
                    else:
                        rolls += self.diceRoll(1,int(iSplit[0]), stopat = stopat)
                elif "k" in i:
                    keptRolls = rolls[:]
                    keptRolls = await self.quickSort(keptRolls,stopat)
                    if "kl" in i:
                        keptRolls = keptRolls[-int(i[2:]):]
                    else:
                        keptRolls = keptRolls[:int(i[1:])]
            if keptRolls == []:
                title = sum(rolls)
                showKept = False
            else:
                title = sum(keptRolls)
                showKept = True
            embed = discord.Embed(title = "Roll Result: {}".format(str(title)),
                    description = "Command: `{}`".format(args))
            embed.add_field(name = "Raw Rolls", value = (str(rolls) + 1024 * "​")[:1024])
            if showKept:
                embed.add_field(name = "Kept Rolls",value = (str(keptRolls) + 1024 * "​")[:1024])
            embed.set_footer(text = "{0}#{1}".format(ctx.author.name,ctx.author.discriminator),
                    icon_url = ctx.author.avatar_url)
        await ctx.send(None,embed = embed)

cogs = [Roll]
