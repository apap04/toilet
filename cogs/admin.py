import discord
from discord.ext import commands

client = commands.Bot(command_prefix=None)
bot = discord.Client()

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    #@bot.command()
    #@commands.has_permissions(kick_members=True)
    #async def kick(ctx, member: discord.Member, *, reason=None):
        #"""Kicks a member"""
        #await member.kick("{} has been kicked. " + f'{reason}')

def setup(bot):
    bot.add_cog(Admin(bot))