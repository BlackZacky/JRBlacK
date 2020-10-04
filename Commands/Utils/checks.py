from discord.ext import commands
from Database import database

import discord

guild = database.guild()
check = database.check()

async def whitelist(ctx):
    if check.guild(ctx.guild.id):
        return guild.get_whitelist(ctx.guild.id) == ctx.channel.id
    return False

async def configure_database(ctx):
    if check.guild(ctx.guild.id):
        await ctx.send(embed=discord.Embed(description=f"{ctx.guild.owner}, você precisa configurar o servidor na database.", color=0xef0027))
        return True
    return False