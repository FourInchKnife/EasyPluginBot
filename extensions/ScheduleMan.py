import discord
from discord.ext import commands

def makeIndicator(letter): ## Python magic
	lets="abcdefghijklmnopqrstuvwxyz"
	maked=eval('''"\\U000'''+hex(lets.index(letter)+127462)[2:]+'''"''')
	return maked
class ScheduleMan(commands.Cog):
	def __init__(self,bot,config):
		self.bot=bot
		self.config=config ## Config!
	@commands.command()
	async def poll(self,ctx,*,arg):
		"""Starts a yes/no poll"""
		allButAuthor=[]
		for i in ctx.guild.members:
			if i != ctx.author:
				allButAuthor.append(i)
		pingable=discord.AllowedMentions(everyone=ctx.author.permissions_in(ctx.channel).mention_everyone,roles=ctx.author.permissions_in(ctx.channel).mention_everyone,users=allButAuthor)
		toEmbed=discord.Embed(title=arg,description="React to this message to tell {0} what works.".format(ctx.author.name),colour=discord.Colour(0xFFFFFF))
		if "@everyone" in arg:
			send="@everyone"
		else:
			send=None
		sent_message=await ctx.send(send,embed=toEmbed,allowed_mentions=pingable)
		await sent_message.add_reaction('\U00002705')
		await sent_message.add_reaction('\U0000274C')
		await ctx.message.delete()
	@commands.command()
	async def days(self,ctx,*,arg):
		"""Polls what days people can do something, whatever that may be"""
		with ctx.channel.typing():
			allButAuthor=[]
			for i in ctx.guild.members:
				if i != ctx.author:
					allButAuthor.append(i)
			pingable=discord.AllowedMentions(everyone=ctx.author.permissions_in(ctx.channel).mention_everyone,roles=ctx.author.permissions_in(ctx.channel).mention_everyone,users=allButAuthor)
			toEmbed=discord.Embed(title=arg,description="React to this message to tell {0} what works.".format(ctx.author.name),colour=discord.Colour(0xFFFFFF))
			if "@everyone" in arg:
				send="@everyone"
			else:
				send=None
			sent_message=await ctx.send(send,embed=toEmbed,allowed_mentions=pingable)
			for i in "mtwhfs":
				await sent_message.add_reaction(makeIndicator(i))
			await sent_message.add_reaction('\U0000274C')
			await ctx.message.delete()

cogs=[ScheduleMan]
