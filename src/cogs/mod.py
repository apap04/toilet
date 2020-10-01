# Copyright (c) 2020 tx3

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

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
