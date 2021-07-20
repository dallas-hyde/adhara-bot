from discord.ext import commands
import requests
import json


class Warframe(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	

	@commands.command(pass_context=True, aliases=["baro"])
	async def baro_kiteer(self, ctx, platform="pc"):
		# Query the warframestat.us API for baro kiteer data on the supplied platform
		response = requests.get(("https://api.warframestat.us/{0}/voidTrader").format(platform))

		# If the response is valid, decode it and get the baro kiteer data from the decoded resposne and send a message with the relevant data
		if response:
			decoded_response = json.loads(response.content)

			# Get relevant void trader information here so the message line isn't as cluttered
			baro_location = decoded_response.get("location")
			baro_start_time = decoded_response.get("startString")
			baro_end_time = decoded_response.get("endString")
			baro_inventory = decoded_response.get("inventory")

			await ctx.send("Baro Ki'Teer:\n\tPlatform:\t`{0}`\n\tLocation:\t`{1}`\n\tStart Time:\t`{2}`\n\tEnd Time:\t`{3}`\n\tInventory:\t`{4}`".format(platform, baro_location, baro_start_time, baro_end_time, baro_inventory))
		
		# If the response was not valid, send an error message
		else:
			await ctx.send("There was a problem retrieving Baro Ki'Teer data!\nPlease try again later. 😟")
	
	
	@commands.command(pass_context=True, aliases=["earth"])
	async def earth_time(self, ctx, platform="pc"):
		# https://api.warframestat.us/{platform}/earthCycle
		pass


	@commands.command(pass_context=True, aliases=["plains", "eidolon"])
	async def plains_of_eidolon(self, ctx, platform="pc"):
		# https://api.warframestat.us/{platform}/cetusCycle
		pass


	@commands.command(pass_context=True, aliases=["orb", "vallis"])
	async def orb_vallis(self, ctx, platform="pc"):
		# https://api.warframestat.us/{platform}/vallisCycle
		pass


	@commands.command(pass_context=True, aliases=["cambion", "drift"])
	async def cambion_drift(self, ctx, platform="pc"):
		# https://api.warframestat.us/{platform}/cambionCycle
		pass
