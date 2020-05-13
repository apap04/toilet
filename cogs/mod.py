import discord
from discord.ext import commands
from utils import permissions, default

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @permissions.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason: str = None):
        """ Kicks a user from the current server. """
        if await permissions.check_priv(ctx, member):
            return
        try:
            await member.kick(reason=default.responsible(ctx.author, reason))
            await ctx.send("kicked " + member + " for " + reason)
        except Exception:
            pass # the command works but we throw on kick without reason! we won't print because of this...

    @commands.command()
    @commands.guild_only()
    @permissions.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason: str = None):
        """ Bans user from the server """
        if await permissions.check_priv(ctx, member):
            return
        try:
            await member.ban(reason=default.responsible(ctx.author, reason))
            await ctx.send("banned " + member + " for " + reason)
        except Exception:
            pass # the command works but we throw on ban without reason! we won't print because of this...

    @commands.command()
    @commands.guild_only()
    @permissions.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        """ 
        Delete a specific amount of messages. Fails if you don't have perms. 
        """
        try:
            await ctx.channel.purge(limit=amount + 1)
        except discord.Forbidden:
            await ctx.send("i don\'t have permissions to flush messages down the toilet.")


def setup(bot):
    bot.add_cog(Mod(bot))
