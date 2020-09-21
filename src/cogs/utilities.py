import discord
import subprocess

from discord.ext import commands
from utils.default import traceback_maker

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="ping")
    async def _ping(self, ctx, address):
        process = subprocess.Popen(["ping", f"{address}"], stdout=subprocess.PIPE)
        while True:
            result: str = process.stdout.readline()
            if not result:
                await ctx.send("pinging..")
            await ctx.send("```\n" + result.rstrip() + "\n```")

def setup(bot):
    bot.add_cog(Utilities(bot))
