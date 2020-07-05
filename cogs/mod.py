# toilet
# Copyright (C) 2019 tx3

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

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
