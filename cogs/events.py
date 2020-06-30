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
import psutil
import os

from datetime import datetime
from discord.ext import commands
from discord.ext.commands import errors
from utils import default


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.process = psutil.Process(os.getpid())

    @commands.Cog.listener()
    async def on_command_error(self, ctx, err):
        if isinstance(err, errors.MissingRequiredArgument) or isinstance(err, errors.BadArgument):
            helper = str(ctx.invoked_subcommand) if ctx.invoked_subcommand else str(ctx.command)
            await ctx.send_help(helper)

        elif isinstance(err, errors.CommandInvokeError):
            error = default.traceback_maker(err.original)

            if "2000 or fewer" in str(err) and len(ctx.message.clean_content) > 1900:
                return await ctx.send(
                    f"You attempted to make the command display more than 2,000 characters...\n"
                    f"Both error and command will be ignored."
                )

            await ctx.send(f"oops. big oops.\n{error}\nthis shouldn't happen. do `poo support` and tell <@403308385539194880> about this...")

        elif isinstance(err, errors.CheckFailure):
            pass

        # elif isinstance(err, errors.MaxConcurrencyReached):
        #     await ctx.send(f"you're using too many commands at once, finish the last one wtf.")

        elif isinstance(err, errors.CommandOnCooldown):
            await ctx.send(f"you're on cooldown. try again in {err.retry_after:.2f} seconds.")

        elif isinstance(err, errors.CommandNotFound):
            pass

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        if not self.config.join_message:
            return

        try:
            to_send = sorted([chan for chan in guild.channels if chan.permissions_for(guild.me).send_messages and isinstance(chan, discord.TextChannel)], key=lambda x: x.position)[0]
        except IndexError:
            pass
        else:
            await to_send.send(self.config.join_message)


    @commands.Cog.listener()
    async def on_message(self, ctx):
        try:
            print(f"{ctx.guild.name} > #{ctx.channel.name} > {ctx.author} > {ctx.clean_content}")
        except AttributeError:
            print(f"Private message > {ctx.author} > {ctx.clean_content}")

    @commands.Cog.listener()
    async def on_ready(self):
        """ The function that actiavtes when boot was completed """
        if not hasattr(self.bot, 'uptime'):
            self.bot.uptime = datetime.utcnow()

        # Indicate that the bot has successfully booted up
        print(f'Ready: {self.bot.user} | Servers: {len(self.bot.guilds)}')

        # Check if user desires to have something other than online
        if self.config.status_type == "idle":
            status_type = discord.Status.idle
        elif self.config.status_type == "dnd":
            status_type = discord.Status.dnd
        else:
            status_type = discord.Status.online

        # Check if user desires to have a different type of playing status
        if self.config.playing_type == "listening":
            playing_type = 2
        elif self.config.playing_type == "watching":
            playing_type = 3
        else:
            playing_type = 0

        await self.bot.change_presence(
            activity=discord.Activity(type=playing_type, name=self.config.playing),
            status=status_type
        )

def setup(bot):
    bot.add_cog(Events(bot))