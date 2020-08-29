# Toilet

Toilet is a Discord bot based off of AlexFlipnote's base with an extended amount of commands.

## Hosting

You are free to use anything to host the bot. The official bot instance is hosted on Heroku.

## Running the bot

To run the bot, you need the [latest version of Python](https://www.python.org/ftp/python/3.8.5/python-3.8.5.exe)
and you must follow these steps
   1. Inside the `src` folder, copy `config.json.example` and rename it to `config.json`
   2. Change these values
      1. Status types are `online`, `idle`, `dnd`
      2. Playing types are `playing`, `listening` and `watching`
      3. The owners list should have your user ID, this allows you to use admin commands in [`src\cogs\admin`](./src/cogs/admin.py)
      4. `join_message` is used for the join message when the bot joins a guild
      5. `token` is for signing in the bot.
   3. Install the required deps using `python3 -m pip install -r requirements.txt`
   4. Finally, run `python3 .\src\main.py`

You can also make a script to do this for you.

## Troubleshooting

### I'm getting this error: `TypeError: __new__() got an unexpected keyword argument 'deny_new'`, pls help!!

Upgrade discord.py. Run `python3 -m pip install -U discord.py`.
