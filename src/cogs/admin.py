# Copyright (c) 2020 tx3

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# Credit to @AlexFlipnote for portions of this code! :))

import discord
from discord.ext import commands
import os
import sys
import time
from utils import permissions, default, http, dataIO

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("src/config.json")
        self._last_result = None

    @commands.command(hidden=True)
    @commands.check(permissions.is_owner)
    async def load(self, ctx, name: str):
        """ Loads an extension. """
        try:
            self.bot.load_extension(f"cogs.{name}")
        except Exception as e:
            return await ctx.send(default.traceback_maker(e))
        await ctx.send(f"Loaded extension **{name}.py**")

    @commands.command(hidden=True)
    @commands.check(permissions.is_owner)
    async def unload(self, ctx, name: str):
        """ Unloads an extension. """
        try:
            self.bot.unload_extension(f"cogs.{name}")
        except Exception as e:
            return await ctx.send(default.traceback_maker(e))
        await ctx.send(f"Unloaded extension **{name}.py**")

    @commands.command(hidden=True)
    @commands.check(permissions.is_owner)
    async def reload(self, ctx, name: str):
        """ Reloads an extension. """
        try:
            self.bot.reload_extension(f"cogs.{name}")
        except Exception as e:
            return await ctx.send(default.traceback_maker(e))
        await ctx.send(f"Reloaded extension **{name}.py**")

    @commands.command(hidden=True)
    @commands.check(permissions.is_owner)
    async def die(self, ctx):
        """uea"""
        await ctx.send('gn')
        time.sleep(1)
        sys.exit(0)

    @commands.command(hidden=True)
    @commands.check(permissions.is_owner)
    async def dm(self, ctx, user_id: int, *, message: str):
        """dm someone for the trollz"""
        user = self.bot.get_user(user_id)
        if not user:
            return await ctx.send(f"can't find mr **{user_id}**")
        try:
            await user.send(message)
            await ctx.send(f"messaged **{user_id}**")
        except discord.Forbidden:
            await ctx.send("he don't wanna talk :neutral_face:")

    @commands.group(hidden=True)
    @commands.check(permissions.is_owner)
    async def change(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send_help(str(ctx.command))

    @change.command(name="playing")
    @commands.check(permissions.is_owner)
    async def change_playing(self, ctx, *, playing: str):
        """playing stats chang8r for whatever reason"""
        if self.config.status_type == "idle":
            status_type = discord.Status.idle
        elif self.config.status_type == "dnd":
            status_type = discord.Status.dnd
        else:
            status_type = discord.Status.online

        if self.config.playing_type == "listening":
            playing_type = 2
        elif self.config.playing_type == "watching":
            playing_type = 3
        else:
            playing_type = 0

        try:
            await self.bot.change_presence(
                activity=discord.Activity(type=playing_type, name=playing),
                status=status_type
            )
            dataIO.change_value(self.config, "playing", playing)
            await ctx.send("changed gamer status to " + f'**{playing}**.')
        except discord.InvalidArgument as err:
            await ctx.send(err)
        except Exception as e:
            await ctx.send(e)

    @change.command(name="username")
    @commands.check(permissions.is_owner)
    async def change_username(self, ctx, *, name: str):
        """change username ;)"""
        try:
            await self.bot.user.edit(username=name)
            await ctx.send(f"yea aight now i'm **{name}** :sob:")
        except discord.HTTPException as e:
            await ctx.send("too many people might have this name, try something else.")
            print(f"exception at {e}")


def setup(bot):
    bot.add_cog(Admin(bot))
