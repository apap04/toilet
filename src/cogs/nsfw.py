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
import rule34
import asyncio
import aiohttp
import random

from discord.ext import commands


class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.command()
    # @commands.guild_only()
    # @commands.is_nsfw()
    # async def r34(self, ctx, *, tags: str):
    #     """ Get hentai from rule34.xxx. """
    #     loop = asyncio.get_event_loop()
    #     r34 = rule34.Rule34(loop=loop)
    #     try:
    #         urls = await r34.getImages(tags, singlePage=True, randomPID=True)
    #         chosen = random.choice([urls])
    #         print(chosen)
    #         await ctx.send(chosen)
    #     except Exception as e:
    #         print(e)
    #         await ctx.send("try something else, that didn't work :(")
    #         # pass #some strings won't work, we'll just pass


def setup(bot):
    bot.add_cog(NSFW(bot))
