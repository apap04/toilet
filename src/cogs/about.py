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
import psutil
import os
from discord.ext import commands
from utils import default
from datetime import datetime

class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("src/config.json")
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
            name="Servers", value=f"{len(ctx.bot.guilds)} ( averaging: {avgmembers} users/server )", inline=True)
        embed.add_field(name="Commands loaded", value=len(
            [x.name for x in self.bot.commands]), inline=True)
        embed.add_field(name="RAM usage", value=f"{ramUsage:.2f} MB", inline=True)

        await ctx.send(content=f"about **{ctx.bot.user}** | **{self.config.version}**", embed=embed)

    @commands.command()
    async def source(self, ctx):
        """ Bot source info """
        embed = discord.Embed(
            title="the plumbing behind the toilet",
            description="The cool tech that makes the toilet work!\n")
        embed.add_field(name="Source", value="https://gitlab.com/toilet/toilet", inline=True)
        embed.add_field(name="Powered by", value="https://github.com/AlexFlipnote/discord_bot.py/", inline=True)

        await ctx.send("the sauce..", embed=embed)

def setup(bot):
    bot.add_cog(About(bot))
