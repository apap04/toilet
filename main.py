#!/usr/bin/env python3 

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
import os
import logging
import random
import argparse
from utils import permissions, default, http, dataIO

# try:
#   import googleclouddebugger
#   googleclouddebugger.enable()
# except ImportError:
#    pass

parser = argparse.ArgumentParser(description='le epic bot everyone will like.')
parser.add_argument("--log", choices=["debug", "dinfo", "info"], help="specific logging flags. this will change game and token values!!")
quotes = ["reee", "ready to flush owo", "poop", "poop funny!", "OwO what's this?", "h", "um :flushed:", "The token is 5."]

args = parser.parse_args()
logger = args.log
logging.basicConfig(level=logging.INFO)

if logger == "debug":
    logging.basicConfig(level=logging.DEBUG)

client = discord.Client()
bot = commands.Bot(command_prefix='pp ', description="the bathroom utility (toilet paper not included)",
                   owner_id="138056116880932864")

# region
@bot.event
async def on_ready():
    print("\n" + random.choice(quotes) + "\n")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandError):
        print(error)
    if isinstance(error, commands.CheckFailure):
        await ctx.send("you can't use this command.")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("you're missing an argument.")
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send("i'm missing permissions. nice job.")
    if isinstance(error, commands.ExtensionNotLoaded):
        await ctx.send("couldn\'t load extension")

@bot.command(hidden=True)
@commands.check(permissions.is_owner)
async def l(ctx, extension):
    """Loads a command"""
    bot.load_extension(f'cogs.{extension}')
    print("Loaded " + f'{extension}!')
    await ctx.send("loaded " + f'{extension}.')

@bot.command(hidden=True)
@commands.check(permissions.is_owner)
async def u(ctx, extension):
    """Unloads a command"""
    bot.unload_extension(f'cogs.{extension}')
    print("Unloaded " + f'{extension}!')
    await ctx.send("unloaded " + f'{extension}.')

@bot.command(hidden=True)
@commands.check(permissions.is_owner)
async def r(ctx, extension):
    """Reloads a command"""
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    print("Reloaded " + f'{extension}!')
    await ctx.send("reloaded " + f'{extension}.')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(os.environ['TOKEN'])
