# Copyright (c) 2020 tx3

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

import os
import random

from utils import default
from utils.data import Bot, HelpFormat

quotes = ["reee", "ready to flush owo", "poop", "poop funny!",
        "OwO what's this?", "h", "um :flushed:", "The token is 5."]

config = default.get("src/config.json")
print("---", random.choice(quotes), "---")

bot = Bot(
    command_prefix=config.prefix,
    prefix=config.prefix,
    command_attrs=dict(hidden=True),
    help_command=HelpFormat()
)

for file in os.listdir("src/cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")

bot.run(config.token)
