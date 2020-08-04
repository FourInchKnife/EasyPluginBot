import os
import importlib
import discord
from discord.ext import commands
from time import sleep

#setup variables
abort_on_no_extensions=True #stops the bot from running if no extensions are loaded
bot_command_prefix="!" #sets the prefix for all commands tied to the bot
directory="examples" #sets the directory for extensions

bot = commands.Bot(command_prefix=commands.when_mentioned_or(bot_command_prefix))

print("Checking "+directory+"/ for extensions...")
for i in os.listdir(directory):
    if i.endswith(".py"):
        print("Searching {} for cogs...".format(i))
        file=importlib.import_module(directory+"."+i[:-3])
        try:
            for k in file.cogs:
                bot.add_cog(k(bot))
                print("| Found ",k)
        except NameError:
            print('Improper extension file, missing "cogs" variable. Ignoring and moving on.')
if bot.cogs == {}:
    print("No extensions found.")
    if abort_on_no_extensions:
        print("Aborting in 5 seconds...")
        sleep(5)
        exit()

@bot.event
async def on_connect():
    print("Logged in as {0}".format(bot.user))

@bot.event
async def on_command_error(ctx,err):
    if type(err)!=commands.errors.CommandNotFound:
        await ctx.send(err)

bot_token=os.environ.get('bot_token')
if not bot_token:
    bot_token=input('What is your bot token?')
bot.run(bot_token)
