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
import lyricsgenius
import os
import rule34
import asyncio
import aiohttp
import io
import random
import urllib
import json

from discord.ext import commands
from utils import default

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def genius(self, ctx, *, song: str):
        """
        [WIP] Sends you lyrics your way!
        """
        try:
            genius = lyricsgenius.Genius(os.environ["GENIUS_TOKEN"])
            song = genius.search_song(f"{song}")
            embed = discord.Embed(title=song.title + " by " + song.artist,
                                  description=f"Full lyrics: {song.url}\n\n {song.lyrics}.."[0:997])
            await ctx.send(embed=embed)
        except KeyError:
            await ctx.send("i couldn't find a Genius key in my environment...")

    @commands.command()
    @commands.guild_only()
    @commands.is_nsfw()
    async def r34(self, ctx, *, tags: str = None):
        """ Get hentai from rule34.xxx. """
        loop = asyncio.get_event_loop()
        r34 = rule34.Rule34(loop=loop)
        urls = await r34.getImageURLS(tags, singlePage=True, randomPID=True)
        try:
            chosen = random.choice(urls)
            await ctx.send(chosen)
        except Exception:
            await ctx.send("try something else, that didn't work :(")
            #pass #some strings won't work, we'll just pass

    @commands.command(name="xkcd")
    @commands.guild_only()
    async def get_lastest_xkcd(self, ctx, comic: int = None):
        """
        Get the latest (or any) xkcd comic!
        """
        try:
            if comic == None:
                with urllib.request.urlopen("https://xkcd.com/info.0.json") as url:
                    data = json.loads(url.read().decode())
                    result = f"**{data['safe_title']}**\n*\"{data['alt']}\"*\n{data['img']}"
                    # turn this into an embed!
                    await ctx.send(result)
            else:
                with urllib.request.urlopen(f"https://xkcd.com/{comic}/info.0.json") as url:
                    data = json.loads(url.read().decode())
                    result = f"**{data['safe_title']}**\n*\"{data['alt']}\"*\n{data['img']}"
                    # turn this into an embed!
                    await ctx.send(result)
        except Exception as e:
            await ctx.send(e)

def setup(bot):
    bot.add_cog(Fun(bot))
