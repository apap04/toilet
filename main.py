import os
import random

from utils import default
from utils.data import Bot, HelpFormat

quotes = ["reee", "ready to flush owo", "poop", "poop funny!", "OwO what's this?", "h", "um :flushed:", "The token is 5."]

config = default.get("config.json")
print("---", random.choice(quotes), "---")

bot = Bot(
    command_prefix=config.prefix,
    prefix=config.prefix,
    command_attrs=dict(hidden=True),
    help_command=HelpFormat()
)

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")

bot.run(config.token)
