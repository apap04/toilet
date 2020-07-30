import discord
import rule34
import asyncio
import aiohttp
import random

from utils.pornhub.pornhub import PornHub
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

    @commands.command(name="phub")
    @commands.guild_only()
    @commands.is_nsfw()
    async def get_porn(self, ctx, *, query: str = None):
        try:
            keywords = ["fortnite"]
            client = PornHub(keywords)
            for videos in client.getVideos(1, random.randint(1, 10)):
                await ctx.send(videos["url"])
        except Exception as e:
            print(e)


def setup(bot):
    bot.add_cog(NSFW(bot))
