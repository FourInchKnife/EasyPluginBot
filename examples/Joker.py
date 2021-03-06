import discord
from discord.ext import commands
import random


class Joker(commands.Cog):
    def __init__(self,bot,config,key):
        self.bot=bot
        self.jokes=config["jokelist"]
        self.comparisons=config["comparisons"]
        self.usedjokes=[]
    @commands.command()
    async def joke(self,ctx):
        """Tells a HORRIBLE joke"""
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
        await ctx.send(first+" "+random.choice(self.comparisons)+" "+second,allowed_mentions=discord.AllowedMentions(everyone=False,roles=False,users=False))
    @commands.command()
    async def slap(self,ctx,people: commands.Greedy[discord.Member],*,reason="a good reason!"):
        if len(people)==1:
            slapstr=people[0].mention
        elif len(people)==2:
            slapstr=people[0].mention+" and "+people[1].mention
        else:
            slapstr=""
            for i in people:
                if i != people[-1]:
                    slapstr+=i.mention+", "
                else:
                    slapstr+="and "+i.mention
        await ctx.send("Slapped {} for {}".format(slapstr,reason),allowed_mentions=discord.AllowedMentions(everyone=False,users=False,roles=False))
        try:
            await ctx.message.delete()
        except:
            pass

cogs=[Joker]
