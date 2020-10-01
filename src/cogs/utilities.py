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
import subprocess

from discord.ext import commands
from utils.default import traceback_maker

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="ping")
    async def _ping(self, ctx, address):
        process = subprocess.Popen(["ping", f"{address}"], stdout=subprocess.PIPE)
        while True:
            result: str = process.stdout.readline()
            if not result:
                await ctx.send("pinging..")
            await ctx.send("```\n" + result.rstrip() + "\n```")

def setup(bot):
    bot.add_cog(Utilities(bot))
