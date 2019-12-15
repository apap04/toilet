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

parser = argparse.ArgumentParser(description='le epic bot everyone will like.')
parser.add_argument("--log", choices=["debug", "info"], help="specific logging flags. this will change game and token values!!")
quotes = ["reee", "ready to flush owo", "poop", "poop funny!", "OwO what's this?"]

args = parser.parse_args()
logger = args.log

if logger == "debug":
    logging.basicConfig(level=logging.DEBUG)
    token = "NjE0MTQzODUwODQ3NTM1MTE0.Xfaa_g.aNOIs_1aUecAJ6B7XBvPVQ6bTkY"
    gameval = "pphelp | toilet.apap04.com"

elif logger == "info":
    logging.basicConfig(level=logging.INFO)
    token = os.environ['TOKEN']
    gameval = os.environ['IS_PLAYING']

client = discord.Client()
bot = commands.Bot(command_prefix='pp', description="the bathroom utility (toilet paper not included)",
                   owner_id="138056116880932864")
game = discord.Game(gameval)

# region
@bot.event
async def on_ready():
    print("\n" + random.choice(quotes) + "\n")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandError):
        print(error)
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You can't use this command.")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You're missing an argument.")
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send("I'm missing permissions. Nice job.")
# endregion

def am_me(ctx):
    return ctx.author.id == 138056116880932864

# utility commands
@bot.command(hidden=True)
@commands.check(am_me)
async def l(ctx, extension):
    """Loads a command"""
    bot.load_extension(f'cogs.{extension}')
    print("Loaded " + f'{extension}')

@bot.command(hidden=True)
@commands.check(am_me)
async def u(ctx, extension):
    """Unloads a command"""
    bot.unload_extension(f'cogs.{extension}')
    print("Unloaded " + f'{extension}')

@bot.command(hidden=True)
@commands.check(am_me)
async def r(ctx, extension):
    """Reloads a command"""
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    print("Reloaded " + f'{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(token)