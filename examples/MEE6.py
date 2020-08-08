'''
The goal of this extension is to be a MEE6 clone with all of the non voice components for free.
'''
import discord
from discord.ext import commands
import importlib
import os
import threading

def makeIndicator(letter): ## Python magic
	'''Generates the correct regional indicator emoji for a letter'''
	lets="abcdefghijklmnopqrstuvwxyz"
	maked=eval('''"\\U000'''+hex(lets.index(letter)+127462)[2:]+'''"''')
	return maked

class Moderation(commands.Cog):
    def __init__(self, bot, config,key):
        self.bot=bot
        self.config=config
        serverfile=importlib.import_module("serverutils")
        t=threading.Thread(target=serverfile.run)
        t.start()
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

cogs = [Moderation]
