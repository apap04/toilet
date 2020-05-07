import discord
import psutil
import os
from discord.ext import commands
from utils import default
from datetime import datetime


class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.process = psutil.Process(os.getpid())

    @commands.command()
    async def support(self, ctx):
        """ Support server link """
        if ctx.guild.id != 707793959338115182:
            return await ctx.send("need help? join https://discord.gg/YPg8dhM")
        elif ctx.guild.id == 707793959338115182:
            return await ctx.send("u already in here")

    @commands.command(aliases=['info', 'stats', 'status'])
    async def about(self, ctx):
        """ About the bot """
        ramUsage = self.process.memory_full_info().rss / 1024**2
        avgmembers = round(len(self.bot.users) / len(self.bot.guilds))

        embedColour = discord.Embed.Empty
        if hasattr(ctx, 'guild') and ctx.guild is not None:
            embedColour = ctx.me.top_role.colour

        embed = discord.Embed(colour=embedColour)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        # embed.add_field(name="Last boot", value=default.timeago(
        #     datetime.now() - self.bot.uptime), inline=True)
        embed.add_field(
            name=f"Developer{'' if len(self.config.owners) == 1 else 's'}",
            value=', '.join([str(self.bot.get_user(x))
                             for x in self.config.owners]),
            inline=True)
        embed.add_field(name="Library", value="discord.py", inline=True)
        embed.add_field(
            name="Servers", value=f"{len(ctx.bot.guilds)} ( avg: {avgmembers} users/server )", inline=True)
        embed.add_field(name="Commands loaded", value=len(
            [x.name for x in self.bot.commands]), inline=True)
        embed.add_field(name="RAM", value=f"{ramUsage:.2f} MB", inline=True)

        await ctx.send(content=f"ℹ About **{ctx.bot.user}** | **{self.config.version}**", embed=embed)

    @commands.command()
    async def source(self, ctx):
        """ Bot source info """
        embed = discord.Embed(title="the plumbing behind the toilet")
        embed.add_field(name="Source", value="https://gitlab.com/toilet/toilet")
        embed.add_field(name="Partly powered by", value="https://github.com/AlexFlipnote/discord_bot.py/tree/master/utils")

        await ctx.send("the sauce..", embed=embed)

def setup(bot):
    bot.add_cog(About(bot))