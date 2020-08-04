import os
import importlib
import discord
from discord.ext import commands
from time import sleep
import json

with open("config.json","r") as file:
    config = json.loads(file.read())

#setup variables
abort_on_no_extensions=config["bot"]["no_ext_abort"] #stops the bot from running if no extensions are loaded
bot_command_prefix=config["bot"]["command_prefix"] #sets the prefix for all commands tied to the bot
directory=config["bot"]["ext_dir"] #sets the directory for extensions
owner_discord_id=set(config["bot"]["owner_ids"]) #sets the discord id of the owner(s) of the bot. defaults to clyde (an official discord account)
bot_token=config["bot"]["bot_token"]

bot = commands.Bot(command_prefix=commands.when_mentioned_or(bot_command_prefix),owner_ids=owner_discord_id)

print("Checking "+directory+"/ for extensions...")
for i in os.listdir(directory):
    if i.endswith(".py"):
        print("Searching {} for cogs...".format(i))
        try:
            file=importlib.import_module(directory+"."+i[:-3])
            try:
                for k in file.cogs:
                    bot.add_cog(k(bot,config["ext"][k.__name__])) ## Allow cogs to have config, without opening files multiple times
                    print("| Found ",k)
            except NameError:
                print('Improper extension file, missing "cogs" variable. Ignoring and skipping file.')
        except Exception as e:
            print("Exception: {} in {}. Ignoring and skipping file.".format(e,file))
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

if not bot_token:
    bot_token=os.environ.get('bot_token')
if not bot_token:
    bot_token=input('What is your bot token?')

bot.run(bot_token)
