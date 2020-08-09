import discord
import rule34
import asyncio
import aiohttp
import random

from discord.ext import commands

class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.is_nsfw()
    async def r34(self, ctx, *, tags: str):
        """ Get hentai from rule34.xxx. """
        loop = asyncio.get_event_loop()
        r34 = rule34.Rule34(loop=loop)
        urls = await r34.getImageURLS(tags, singlePage=True, randomPID=True)
        try:
            chosen = random.choice(urls)
            await ctx.send(chosen)
        except Exception:
            await ctx.send("try something else, that didn't work :(")
            # pass #some strings won't work, we'll just pass

def setup(bot):
    bot.add_cog(NSFW(bot))
