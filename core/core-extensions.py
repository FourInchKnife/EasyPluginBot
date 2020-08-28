import discord
from discord.ext import commands

class Core(commands.Cog):
	def __init__(self,bot,config):
		self.bot = bot
		self.config = config
	def listStr(self,listIn):
		strOut=""
		if len(listIn)==1:
			strOut=listIn[0]
		elif len(listIn)==2:
			strOut=f"{listIn[0]} and {listIn[1]}"
		else:
			for i in listIn[:-1]:
				strOut+=i+", "
			strOut+="and "+listIn[-1]
		return strOut
	@commands.command()
	async def info(self, ctx):
		embed = discord.Embed(title="Bot Info")
		ownerNames=[]
		for i in self.config["owner_ids"]:
			tempUser= await self.bot.fetch_user(i)
			try:
				ownerNames.append(str(tempUser))
			except:
				ownerNames.append("Unknown")
		embed.add_field(name="Owner(s)",value=self.listStr(ownerNames))
		cogNames=[]
		for i in self.bot.cogs:
			cogNames.append(i)
		embed.add_field(name="Extension(s)",value=self.listStr(cogNames))
		links=[]
		for i in self.config["links"]:
			links.append("[{0}]({1})".format(i, self.config["links"][i]))
		embed.add_field(name="GitHub",value="\n".join(links))
		await ctx.send(None,embed=embed)

cogs=[Core]
