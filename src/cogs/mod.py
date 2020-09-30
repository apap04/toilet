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
        """
        Kicks a user from the current server.
        """
        try:
            if await permissions.check_priv(ctx, member):
                return
            await ctx.send(
                f"kicked {str(member)} for no reason."
                if reason is None
                else f'kicked {str(member)} for "{reason}".'
            )
            await member.kick(reason=default.responsible(ctx.author, reason))
        except Exception as e:
            await ctx.send("nevermind, i don't have permissions.")
            print(e)

    @commands.command()
    @commands.guild_only()
    @permissions.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason: str = None):
        """
        Bans user from the server
        """
        try:
            if await permissions.check_priv(ctx, member):
                return
            await ctx.send(
                f"banned {str(member)} for no reason."
                if reason is None
                else f'banned {str(member)} for "{reason}".'
            )
            await member.ban(reason=default.responsible(ctx.author, reason))
        except Exception as e:
            await ctx.send("nevermind, i don't have permissions.")
            print(e)

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
            await ctx.send(
                "i don't have permissions to flush messages down the toilet."
            )

    @commands.group()
    @commands.guild_only()
    @permissions.has_permissions(manage_roles=True)
    async def role(self, ctx, member: discord.Member):
        """
        Do something with the roles.
        """
        if ctx.invoked_subcommand is None:
            await ctx.send_help(str(ctx.command))

    @role.command(name="add")
    @commands.guild_only()
    @permissions.has_permissions(manage_roles=True)
    async def create_role(self, ctx, *, role: str, color: discord.Color = None):
        """
        Create a new role, the quick way.
        """
        try:
            if await permissions.check_priv(ctx, member):
                return
            await ctx.guild.create_role(name=role)
            await ctx.send(f"created role {role}")
        except discord.Forbidden:
            await ctx.send("i can't make roles")

    @role.command(name="give")
    @commands.guild_only()
    #
    async def give_role(parameter_list):
        pass


def setup(bot):
    bot.add_cog(Mod(bot))
