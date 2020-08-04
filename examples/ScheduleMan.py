import discord
from discord.ext import commands

class ScheduleMan(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    @bot.command()
    async def poll(ctx,*,arg):
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
    @bot.command
    async def days(ctx,*,arg):
        with ctx.channel.typing():
            allButAuthor=[]
            for i in ctx.guild.members:
                if i != ctx.author:
                    allButAuthor.append(i)
            pingable=discord.AllowedMentions(everyone=ctx.author.permissions_in(ctx.channel).mention_everyone,roles=ctx.author.permissions_in(ctx.channel).mention_everyone,users=allButAuthor)
            toEmbed=discord.Embed(title=arg,description="React to this message to tell {0} what works."..format(ctx.author.name),colour=discord.Colour(0xFFFFFF))
            if "@everyone" in arg:
                send="@everyone"
            else:
                send=None
            sent_message=await ctx.send(send,embed=toEmbed,allowed_mentions=pingable)
            emojiGuild=bot.get_guild(712731280772694198)
            emojiIDs=[721544022534914130,721544022216278056,721544022534914120,721544022547759165,721544022237249538,721544$        for i in emojiIDs:
                nextEmoji= await emojiGuild.fetch_emoji(i)
                await sent_message.add_reaction(nextEmoji)
            await sent_message.add_reaction('\U0000274C')
            await ctx.message.delete()

cogs=[ScheduleMan]
