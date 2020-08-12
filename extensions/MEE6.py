'''
The goal of this extension is to be a MEE6 clone with all of the non voice components for free.
'''
import discord
from discord.ext import commands
import imp
import os
import multiprocessing

def makeIndicator(letter): ## Python magic
	'''Generates the correct regional indicator emoji for a letter'''
	lets="abcdefghijklmnopqrstuvwxyz"
	maked=eval('''"\\U000'''+hex(lets.index(letter)+127462)[2:]+'''"''')
	return maked

class Moderation(commands.Cog):
	def __init__(self, bot, config=None,keys=None):
		self.bot=bot
	@commands.command()
	async def kick(self, ctx, person: discord.Member, *, reason = ""):
		"""Kicks a member from the server"""
		if not ctx.author.guild_permissions.kick_members:
			return await ctx.send("No.")
		try:
			await person.kick(reason=reason)
			sent_message = await ctx.send("Kicked {}".format(person.mention),allowed_mentions=discord.AllowedMentions(users=False))
			for i in "bye":
				await sent_message.add_reaction(makeIndicator(i))
		except discord.HTTPException:
			await ctx.send("Failed to kick {}. Try making sure that I have the `kick members` permission, or move my role to the top of the list.".format(person.mention),allowed_mentions=discord.AllowedMentions(users=False))
	@commands.command()
	async def ban(self, ctx, person: discord.Member, *, reason = ""):
		"""Bans a member from the server"""
		if not ctx.author.guild_permissions.ban_members:
			return await ctx.send("No.")
		try:
			await person.ban(reason=reason)
			sent_message = await ctx.send("Banned {}".format(person.mention),allowed_mentions=discord.AllowedMentions(users=False))
			for i in "ban":
				await sent_message.add_reaction(makeIndicator(i))
		except discord.HTTPException:
			await ctx.send("Failed to ban {}. Try making sure that I have the `ban members` permission, or move my role to the top of the list.".format(person.mention),allowed_mentions=discord.AllowedMentions(users=False))
class Website(commands.Cog):
	def __init__(self,bot,config,keys=None):
		self.config=config
		self.admins=config["web_admins"]
		serverfile=imp.load_source("server",config["bot"]["ext_dir"]+"/server.py")
		self.status=multiprocessing.Value("i",0)
		self.runserver=multiprocessing.Value("i",1)
		self.port=multiprocessing.Value("i",0)
		self.stopper=None
		self.attemptstoppers=[]
		p=multiprocessing.Process(target=serverfile.run,args=(config["host"],config["port"],self.status,self.runserver,self.port,config["uristerilizerconfig"],config["websendconfig"]))
		p.start()
	@commands.command()
	async def webstatus(self,ctx):
		embed=discord.Embed(title="Webserver Status")
		embed.add_field(name="Server status",value=str({1:"Running",0:"Off"}[self.status.value]))
		if self.status.value==1:
			embed.add_field(name="Port",value=str(self.port.value),inline=False) #do the rest like this... i have to go
			if self.attemptstoppers != []:
				stopperstring=(self.attemptstoppers[0].mention if len(self.attemptstoppers)==1 else "")
				if len(self.attemptstoppers)>1:
					for x in self.attemptstoppers[:-1]:
						stopperstring+=x.mention+", "
					stopperstring+="and "+self.attemptstoppers[-1].mention
				embed.add_field(name="Every person who failed to stop the server",value=stopperstring)
		else:
			embed.add_field(name="Stopped By",value=self.stopper.mention)
		await ctx.send(None,embed=embed)
	@commands.command()
	async def stopserver(self,ctx):
		'''Only hardcoded serveradmins can run this. You are probably not a serveradmin.'''
		if ctx.author.id in self.admins:
			await ctx.send("As you wish.")
			self.runserver.value=0
			self.stopper=ctx.author
		else:
			await ctx.send("You don't have permission to do that. This will be reported.")
			print("USER ATTEMPTED TO RUN UNAUTHORIZED TASK!")
			self.attemptstoppers.append(ctx.author)
cogs = [Moderation,Website]
