from discord.ext import commands
import requests
import json


class Planetside(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    # TODO: Implement command to get server ids and display them so users don't have to look up server ids
    @commands.command(pass_context=True, aliases=["sp", "serverpop"])
    async def server_pop(self, ctx, server_id=17):
        # Query the PS2 FISU API for population data on the supplied server
        response = requests.get("https://ps2.fisu.pw/api/population/?world={0}".format(server_id))

        # If the response is valid, decode it and get the population data from the decoded response and send a message with the server and population data
        if response:
            decoded_response = json.loads(response.content)
            population_data = decoded_response.get("result")[0]

            # Get the population of each faction from the population data so the message send line isn't as cluttered
            vs_population = population_data.get("vs")
            nc_population = population_data.get("nc")
            tr_population = population_data.get("tr")
            ns_population = population_data.get("ns")
            total_population = vs_population + nc_population + tr_population + ns_population

            await ctx.send("Server: {0}\n```VS: {1}\nNC: {2}\nTR: {3}\nNS: {4}\n```Total: {5}".format(server_id, vs_population, nc_population, tr_population, ns_population, total_population))
        
        # If the response was not valid, send an error message
        else:
            await ctx.send("There was a problem retrieving population data!\nPlease try again later. 😟")
