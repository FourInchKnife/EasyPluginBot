from discord.ext import commands
import discord
from random import randint

class Roll(commands.Cog):
    def __init__(self,bot,config,key):
        self.bot = bot
    def diceRoll(self,amount,type):
        rolls = []
        for i in range(amount):
            rolls.append(randint(1,type))
        return rolls
    @commands.command()
    async def roll(self, ctx, *, args):
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
                        rolls += self.diceRoll(iSplit[0],iSplit[1])
                    else:
                        rolls += self.diceRoll(1,iSplit[0])
                elif "k" in i:
                    keptRolls = rolls[:]
                    keptRolls.sort(reverse = True)
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
            embed.add_field(name = "Raw Rolls", value = str(rolls))
            if showKept:
                embed.add_field(name = "Kept Rolls",value = str(keptRolls))
            embed.set_footer(text = "{0}#{1}".format(ctx.author.name,ctx.author.discriminator),
                    icon_url = ctx.author.avatar_url)
            await ctx.send(None,embeds = [embed])
