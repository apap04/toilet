import discord
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, member: discord.Member, *, reason=None):
        """Kicks a member"""
        await member.kick("{} has been kicked. " + f'{reason}'.format(member))

def setup(bot):
    bot.add_cog(Admin(bot))