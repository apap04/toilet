#
# The toilet.
# Made by apap04#3355 (GH/GL: apap04) <me@apap04.com>
#

import discord
from discord.ext import commands
import os
import logging
import random

doken = "redacted uwu" # dev token.
quotes = ["reee", "ready to flush owo", "poop", "poop funny!", "OwO what's this?"]

logging.basicConfig(level=logging.INFO)
client = discord.Client()
bot = commands.Bot(command_prefix="poop ", description="the bathroom utility (toilet paper not included)", owner_id="138056116880932864")

@bot.event
async def on_ready():
    print("\n" + random.choice(quotes) + "\n")

#region
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandError):
        pass
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You can't use this command.")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You're missing an argument.")
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send("I'm missing permissions. Nice job.")
#endregion

def am_me(ctx):
    return ctx.author.id == 138056116880932864

#region
@bot.command(hidden=True)
@commands.check(am_me)
async def l(ctx, extension):
    """Loads a command"""
    bot.load_extension(f'cogs.{extension}')
    print("Loaded "+ f'{extension}')

@bot.command(hidden=True)
@commands.check(am_me)
async def u(ctx, extension):
    """Unloads a command"""
    bot.unload_extension(f'cogs.{extension}')
    print("Unloaded "+ f'{extension}')

@bot.command(hidden=True)
@commands.check(am_me)
async def r(ctx, extension):
    """Reloads a command"""
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    print("Reloaded "+ f'{extension}')
#endregion

@bot.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int):
    """Clears a specific amount of messages"""
    await ctx.channel.purge(limit=amount)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


bot.run('NjE0MTQzODUwODQ3NTM1MTE0.XWGT1g.DHolEt_OOryfzf_uI9UaiiDpaI4')