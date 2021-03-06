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
import lyricsgenius
import os
import urllib
import json
import asyncio
import wikipedia

from discord.ext import commands
from discord.ext.commands import errors
from utils import default, permissions

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

    @commands.command(name="xkcd")
    @commands.guild_only()
    async def _xkcd(self, ctx, comic: int = None):
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
        except Exception:
            pass

    @_xkcd.error
    async def xkcd_handler(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("i need a number")

    @commands.command(name="wiki", hidden=True)
    @commands.check(permissions.is_owner)
    async def get_wikipedia_page(self, ctx, *, query: str):
        """
        Get the contents of a Wikipedia page.
        """
        # TODO: Do not allow template pages or user pages to be indexed.
        # TODO(greek): fix Expecting value: line 1 column 1 (char 0)
        try:
            result = wikipedia.search(query)
            summary = wikipedia.summary(result.summary)
            embed = discord.Embed(title=result.title)

            ctx.send(embed=embed)

        except Exception as e:
            await ctx.send(e)

    @commands.command(name="user")
    async def get_user_info(self, ctx, member: discord.Member = None):
        """
        Get information for a specific user.
        """
        try:
            if member is None:
                member = ctx.author
            embed = discord.Embed(colour=member.color, description=f"{member.mention}")
            embed.set_author(name=str(member), icon_url=member.avatar_url)
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name="Join date", value=f"{member.joined_at}"[0:10])
            embed.add_field(name="Creation date", value=f"{member.created_at}"[0:10])
            embed.add_field(name="Roles", value=", ".join([r.mention for r in member.roles]), inline=False)
            embed.set_footer(text="ID: " + str(member.id))
            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send(e)

def setup(bot):
    bot.add_cog(Fun(bot))
