import discord
from discord.ext import commands

client = commands.Bot(command_prefix=None)

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @client.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(ctx, amount: int):
        await ctx.channel.purge(amount)

def setup(bot):
    bot.add_cog(Admin(bot))