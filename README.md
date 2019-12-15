# Toilet

See [the wiki page](https://wiki.apap04.com/wiki/Toilet) for more general public info.

## Developer stuff

Hello! Welcome to the repo of the Toilet bot. This README will house all the developer stuff that developers need to know. Let's start!

### Hosting

Toilet is hosted on the Heroku free plan, but anybody reading this can host it on whatever plan they choose to. Hosting on the free plan will mean that the bot
will most likely run out of hours and shut down near the end of the month. This shouldn't be a problem if we don't push code when hours have already run out.
If you're planning on hosting the bot yourself, you don't have to use Heroku to host. You can use GCE, CGE, HHH, PP lol idk.

### Running the bot

This is the part everyone wants to get into.... Here's how to run the bot!

1. Download Python 3+
2. Clone the bot
3. `cd` into the bot directory
4. Do `pip install -r requirements.txt` to install stuff that's needed
5. Set the token in the code (if you're hosting, leave the token part as is)
6. HOSTING ONLY: Set your environment variable for your hosting service to `TOKEN`
7. Type `python index.py --log info` to run the bot!

There's more stuff you can do with `index.py`. Do `python index.py -h` for additional arguments you can use to make the stuff in the background make more sense.
