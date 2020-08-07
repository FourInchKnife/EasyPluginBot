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
bot_token=config["bot"]["bot_token"] #the token for the bot

bot = commands.Bot(command_prefix=commands.when_mentioned_or(bot_command_prefix),owner_ids=owner_discord_id) #initializes the bot

print("Checking "+directory+"/ for extensions...")
for i in os.listdir(directory): #searches the extension dir
    if i.endswith(".py"):
        print("Searching {} for cogs...".format(i))
        try:
            file=importlib.import_module(directory+"."+i[:-3]) #imports it if it ends in .py
            try:
                for k in file.cogs:
                    try:
                        bot.add_cog(k(bot,config["ext"][i[:-3]][k.__name__])) #adds all of the files cogs from the cogs variable # Allow cogs to have config, without opening files multiple times
                    except KeyError:
                        bot.add_cog(k(bot))
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

@bot.event #prints the name of the bot user
async def on_connect():
    print("Logged in as {0}".format(bot.user))

@bot.event #command error handling
async def on_command_error(ctx,err):
    if type(err)!=commands.errors.CommandNotFound:
        await ctx.send(err)

if not bot_token:
    bot_token=os.environ.get('bot_token')
if not bot_token:
    bot_token=input('What is your bot token?')

bot.run(bot_token) #runs the bot
