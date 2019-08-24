import discord
from discord.ext import commands

client = commands.Bot(command_prefix=None)

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Admin(bot))