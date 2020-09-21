import discord

from utils import default
from discord.ext import commands

owners = default.get("src/config.json").owners


def is_owner(ctx):
    return ctx.author.id in owners


async def check_permissions(ctx, perms, *, check=all):
    if ctx.author.id in owners:
        return True

    resolved = ctx.channel.permissions_for(ctx.author)
    return check(getattr(resolved, name, None) == value for name, value in perms.items())


def has_permissions(*, check=all, **perms):
    async def pred(ctx):
        return await check_permissions(ctx, perms, check=check)
    return commands.check(pred)


async def check_priv(ctx, member):
    try:
        # Self checks
        if member == ctx.author:
            return await ctx.send(f"you can't {ctx.command.name} yourself.")
        if member.id == ctx.bot.user.id:
            return await ctx.send("YO WTF 😡😡😡😡")

        # Check if user bypasses
        if ctx.author.id == ctx.guild.owner.id:
            return False

        # Now permission check
        if member.id in owners:
            if ctx.author.id not in owners:
                return await ctx.send(f"i can't {ctx.command.name} my dad")
            else:
                pass
        if member.id == ctx.guild.owner.id:
            return await ctx.send(f"the owner has more power to {ctx.command.name} you")
        if ctx.author.top_role == member.top_role:
            return await ctx.send(f"can't {ctx.command.name} someone who has the same permissions as you")
        if ctx.author.top_role < member.top_role:
            return
    except Exception:
        pass


def can_send(ctx):
    return isinstance(ctx.channel, discord.DMChannel) or ctx.channel.permissions_for(ctx.guild.me).send_messages


def can_embed(ctx):
    return isinstance(ctx.channel, discord.DMChannel) or ctx.channel.permissions_for(ctx.guild.me).embed_links


def can_upload(ctx):
    return isinstance(ctx.channel, discord.DMChannel) or ctx.channel.permissions_for(ctx.guild.me).attach_files


def can_react(ctx):
    return isinstance(ctx.channel, discord.DMChannel) or ctx.channel.permissions_for(ctx.guild.me).add_reactions


def is_nsfw(ctx):
    return isinstance(ctx.channel, discord.DMChannel) or ctx.channel.is_nsfw()
