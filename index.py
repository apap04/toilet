import discord

client = discord.Client()

@client.event
async def on_ready():
    print("ready to flush ;)\n")

client.run('NjE0MTE1MjIxOTY3MDc3Mzg2.XV6xZQ.G6TPwqKKG6Z6Fx_TfSqeoZwhxoU')