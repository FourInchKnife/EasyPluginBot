#!/usr/bin/env python3
import os
import importlib
import discord
from discord.ext import commands
from time import sleep
import json
import traceback

with open("config.json","r") as file:
    config = json.loads(file.read())
with open("keys.json","r") as file:
    try:
        keys = json.loads(file.read())
    except Exception as e:
        print("Either key.json doesn't exist or it is invalid: {}".format(e))
        keys = {}
'''
To configure the bot edit these lines in "config.json"
{
  "bot":{
    "no_ext_abort" : true,
    "command_prefix":"!",
    "ext_dir":"extensions",
    "owner_ids":[1]
  }
}

To add keys / to extensions (or the bot) put them in "keys.json"
An example of this can be found in "example keys.json"
'''

bot = commands.Bot(command_prefix=commands.when_mentioned_or(config["bot"]["command_prefix"]),owner_ids=set(config["bot"]["owner_ids"])) #initializes the bot

print("Checking "+config["bot"]["ext_dir"]+"/ for extensions...")
for i in os.listdir(config["bot"]["ext_dir"]): #searches the extension dir
    if i.endswith(".py"):
        print("Searching {} for cogs...".format(i))
        try:
            file=importlib.import_module(config["bot"]["ext_dir"]+"."+i[:-3]) #imports it if it ends in .py
            try:
                for k in file.cogs:
                    try:
                        tempkey=keys["ext"][i[:-3]][k.__name__]
                    except KeyError:
                        tempkey=None
                    try:
                        tempconfig=config["ext"][i[:-3]][k.__name__]
                        tempconfig["bot"]=config["bot"]
                    except (KeyError, TypeError):
                        tempconfig={"bot":config["bot"]}
                    bot.add_cog(k(bot,tempconfig,tempkey)) #adds all of the files cogs from the cogs variable # Allow cogs to have config, without opening files multiple times
                    print("| Found ",k)
            except NameError:
                    print('Improper extension file, missing "cogs" variable. Ignoring and skipping file.')
        except Exception as e:
            print("Exception: {} in {}. Ignoring and skipping file.".format(e,file))
            traceback.print_exc()
if bot.cogs == {}:
    print("No working extensions found.")
    if config["bot"]["no_ext_abort"]:
        print("Aborting in 5 seconds...")
        sleep(5)
        exit()

@commands.command()
async def help(ctx,cog):
    print("The cog (in help) is",cog)
    if cog:
        ctx.send("Sorry, this command is temporarily not found and you would do better to not run it.")
    else:
        ctx.send("I would love to help you with that cog. I'm not going to, if you can't tell.")

@bot.event #prints the name of the bot user
async def on_connect():
    print("Logged in as {0}".format(bot.user))

@bot.event #command error handling
async def on_command_error(ctx,err):
    if type(err)!=commands.errors.CommandNotFound:
        await ctx.send(err)

if keys["bot"]:
    bot_token=keys["bot"]
else:
    bot_token=input('What is your bot token?')

bot.run(bot_token) #runs the bot
