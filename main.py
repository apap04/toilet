import os
import random
import argparse

from utils import default
from utils.data import Bot, HelpFormat

parser = argparse.ArgumentParser(description='le epic bot everyone will like.')
parser.add_argument("--log", choices=["debug", "dinfo", "info"], help="specific logging flags. this will change game and token values!!")
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

#bot.run(config.token)
bot.run(os.environ['TOKEN'])
