'''
The goal of this extension is to be a MEE6 clone with all of the non voice components for free.
'''
import discord
from discord.ext import commands

def makeIndicator(letter): ## Python magic
	'''Generates the correct regional indicator emoji for a letter'''
	lets="abcdefghijklmnopqrstuvwxyz"
	maked=eval('''"\\U000'''+hex(lets.index(letter)+127462)[2:]+'''"''')
	return maked

class Moderation(commands.Cog):
	def __init__(self, bot, config,key):
		self.bot=bot
	@commands.command()
	async def kick(self, ctx, person: discord.Member, *, reason = ""):
		"""Kicks a member form the server"""
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
	def prettylist(self,toFormat):
		formatted=""
		if len(toFormat)==1:
			formatted=toFormat[0]
		elif len(toFormat)==2:
			formatted="{} and {}".format(toFormat[0],toFormat[1])
		else:
			for i in toFormat[:-1]:
				formatted+=i+", "
			formatted+="and "+toFormat[-1]
		return formatted
	@commands.command()
	async def prunerole(self,ctx,prune_role: discord.Role,*,reason="User had a pruned role."):
		if not ctx.author.guild_permissions.kick_members:
			return await ctx.send("You don't have the permissions for that.")
		toPrune=[]
		for i in prune_role.members:
			if not i in toPrune:
				toPrune.append(i)
		failures=[]
		for i in toPrune:
			try:
				await i.kick(reason=reason)
			except discord.HTTPException:
				failures.append(i)
		failedNames=[]
		for i in failures: failedNames.append(i.mention)
		prunedNames=[]
		for i in toPrune:
			if not i.mention in failedNames: prunedNames.append(i.mention)
		embed=discord.Embed(title="Prune Results",description="Results of pruning {} for reason `{}`".format(prune_role.mention,reason))
		if prunedNames!=[]: embed.add_field(name="Pruned:",value=self.prettylist(prunedNames))
		if failures!=[]: embed.add_field(name="Failed:",value=self.prettylist(failedNames))
		await ctx.send(None,embed=embed,allowed_mentions=discord.AllowedMentions(users=False))


cogs = [Moderation]
