from discord.ext import commands
import requests
import json


class Warframe(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	

	@commands.command(pass_context=True, aliases=["baro"])
	async def baro_kiteer(self, ctx, platform="pc"):
		# Query the warframestat.us API for Baro Ki'teer's data on the supplied platform
		response = requests.get(("https://api.warframestat.us/{0}/voidTrader").format(platform))

		# If the response is valid, decode it and get the baro kiteer data from the decoded resposne and send a message with the relevant data
		if response:
			decoded_response = json.loads(response.content)

			# Get relevant void trader information here so the message line isn't as cluttered
			baro_location = decoded_response.get("location")
			baro_start_time = decoded_response.get("startString")
			baro_end_time = decoded_response.get("endString")
			# TODO: Format baro's inventory
			baro_inventory = decoded_response.get("inventory")

			await ctx.send("Baro Ki'Teer:\n\tPlatform:\t`{0}`\n\tLocation:\t`{1}`\n\tStart Time:\t`{2}`\n\tEnd Time:\t`{3}`\n\tInventory:\t`{4}`".format(platform, baro_location, baro_start_time, baro_end_time, baro_inventory))
		
		# If the response was not valid, send an error message
		else:
			await ctx.send("There was a problem retrieving Baro Ki'Teer's data!\nPlease try again later. 😟")
	
	
	@commands.command(pass_context=True, aliases=["earth"])
	async def earth_time(self, ctx, platform="pc"):
		# Query warframestat.us API for Earth's time data on the supplied platform
		response = requests.get(("https://api.warframestat.us/{0}/earthCycle").format(platform))

		# If the response is valid, decode it and send the user a message with the relevant data
		if response:
			decoded_response = json.loads(response.content)

			# Get relevant data here so the message line isn't as cluttered
			earth_state = decoded_response.get("state").capitalize()
			earth_time_left = decoded_response.get("timeLeft")

			await ctx.send("Earth:\n\tTime:\t`{0}`\n\tTime Left:\t`{1}`".format(earth_state, earth_time_left))
		
		# If the response was not valid, send an error message
		else:
			await ctx.send("There was a problem retrieving Earth's data!\nPlease try again later. 😟")


	@commands.command(pass_context=True, aliases=["plains", "eidolon", "cetus"])
	async def plains_of_eidolon(self, ctx, platform="pc"):
		# Query warframestat.us API for Cetus's time data on the supplied platform
		response = requests.get(("https://api.warframestat.us/{0}/cetusCycle").format(platform))

		# If the response is valid, decode it and send the user a message with the relevant data
		if response:
			decoded_response = json.loads(response.content)

			# Get relevant data here so the message line isn't as cluttered
			cetus_state = decoded_response.get("state").capitalize()
			cetus_time_left = decoded_response.get("timeLeft")

			await ctx.send("Plains of Eidolon:\n\tTime:\t`{0}`\n\tTime Left:\t`{1}`".format(cetus_state, cetus_time_left))
		
		# If the response was not valid, send an error message
		else:
			await ctx.send("There was a problem retrieving Cetus' data!\nPlease try again later. 😟")


	@commands.command(pass_context=True, aliases=["orb", "vallis"])
	async def orb_vallis(self, ctx, platform="pc"):
		# Query warframestat.us API for the Orb Vallis' weather data on the supplied platform
		response = requests.get(("https://api.warframestat.us/{0}/vallisCycle").format(platform))

		# If the response is valid, decode it and send the user a message with the relevant data
		if response:
			decoded_response = json.loads(response.content)

			# Get relevant data here so the message line isn't as cluttered
			vallis_state = decoded_response.get("state").capitalize()
			vallis_time_left = decoded_response.get("timeLeft")

			await ctx.send("Orb Vallis:\n\tWeather:\t`{0}`\n\tTime Left:\t`{1}`".format(vallis_state, vallis_time_left))
		
		# If the response was not valid, send an error message
		else:
			await ctx.send("There was a problem retrieving the Orb Vallis' data!\nPlease try again later. 😟")


	@commands.command(pass_context=True, aliases=["cambion", "drift", "deimos"])
	async def cambion_drift(self, ctx, platform="pc"):
		# Query warframestat.us API for the Cambion Drift's state data on the supplied platform
		response = requests.get(("https://api.warframestat.us/{0}/cambionCycle").format(platform))

		# If the response is valid, decode it and send the user a message with the relevant data
		if response:
			decoded_response = json.loads(response.content)

			# Get relevant data here so the message line isn't as cluttered
			# TODO: Get the time remaining using the activation and expiry fields
			cambion_state = decoded_response.get("active").capitalize()

			await ctx.send("Cambion Drift:\n\tState:\t`{0}`".format(cambion_state))
		
		# If the response was not valid, send an error message
		else:
			await ctx.send("There was a problem retrieving the Cambion Drift's data!\nPlease try again later. 😟")
