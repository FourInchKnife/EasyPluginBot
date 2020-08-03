import os
import importlib
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))

for i in os.listdir("extensions"):
    if i.endswith(".py") and not i == "__init__.py":
        file=importlib.import_module("extensions."+i[:-3])
        for k in file.cogs:
            bot.add_cog(k(bot))

@bot.event
async def on_connect():
    print("Logged in as {0}".format(bot.user))

@bot.event
async def on_command_error(ctx,err):
    if type(err)!=commands.errors.CommandNotFound:
        await ctx.send(err)

bot_token=environ.get('bot_token')
if not bot_token:
    bot_token=input('What is your bot token?')
    print('\n'*100)
bot.run(bot_token)
