__author__ = "apap04#3355"
import discord
from discord.ext import commands
import os
import logging
import random

doken = "NjE0MTQzODUwODQ3NTM1MTE0.XV7MMQ.GBg_D1OqCE-ClMeCOoEGlAztCb8" # dev token.
quotes = ["reee", "ready to flush owo", "poop", "poop funny!", "OwO what's this?"]

client = discord.Client()
bot = commands.Bot(command_prefix="toilet ", description="the bathroom utility (toilet paper not included)", owner_id="138056116880932864")

@bot.event
async def on_ready():
    print("\n" + random.choice(quotes) + "\n")

@bot.command(is_owner)
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


@bot.command(is_owner)
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


bot.run(doken)