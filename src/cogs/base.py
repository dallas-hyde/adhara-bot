from discord.ext import commands


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        await ctx.send("Pong!")
    

    @commands.command(pass_context=True)
    async def pong(self, ctx):
        await ctx.send("Ping!")
