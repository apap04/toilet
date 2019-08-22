__author__ = "apap04#3355"
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

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("That command doesn't exist.")
    elif isinstance(error, commands.CommandError):
        await ctx.send("Oh shit, the toilet is clogged!\n```" + f'{error}' + "```If you think this was a bug, copy this text above and send it to apap04#3355")
        print(error)

def am_me(ctx):
    return ctx.author.id == 138056116880932864

@bot.command(hidden=True)
@commands.check(am_me)
async def load(ctx, extension):
    """Loads a command"""
    bot.load_extension(f'cogs.{extension}')
    print("Loaded "+ f'{extension}')

@bot.command(hidden=True)
@commands.check(am_me)
async def unload(ctx, extension):
    """Unloads a command"""
    bot.unload_extension(f'cogs.{extension}')
    print("Unloaded "+ f'{extension}')

@bot.command(hidden=True)
@commands.check(am_me)
async def reload(ctx, extension):
    """Reloads a command"""
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    print("Reloaded "+ f'{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


bot.run(os.environ['TOKEN'])