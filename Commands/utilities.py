from difflib import SequenceMatcher
from discord.ext import commands
from Database import *

from . import sub_commands

import discord
import os

FindUserI = "<:finduser:579131818331340830>"
RightI    = "<:right:579131818066968610>"
SearchI   = "<:search:579131818343792641>"

class MyUtils(commands.Cog, name="Utilidades"):
    def __init__(self, client):
        self.client   = client
        self.check = database.check()
        self.guild = database.guild()

    @commands.group(name="procurar", aliases=["find", "search"], usage="[p]procurar [sub comando]")
    @commands.guild_only()
    async def _search(self, ctx):
        if ctx.invoked_subcommand is None:
            return await sub_commands(self.client, ctx, ctx.command.name)

    @_search.command(name="comando", aliases=["commands", "cog", "command", "comandos"], usage="[p]procurar comando [name]")
    @commands.guild_only()
    async def command(self, ctx, command: str):
        lista = []
        for commands in ctx.bot.commands:
            sequence = SequenceMatcher(None, command, commands.name).ratio()
            if sequence >= 0.5:
                lista.append(f"{RightI} {commands.name}")

        if len(lista) == 0:
            await ctx.send(embed=discord.Embed(color=0xc63939, description=f"{ctx.author.mention}: Não achei nem um comando com este nome ou parecido."))
        else:
            filtro = "\n".join(lista)
            embed = discord.Embed(title=f"{SearchI} Procurar - {ctx.guild.name}", description=f"{filtro}", color=0x4B0082)
            embed.set_footer(text=f"Total de comando(s) achado(s) {len(lista)}")
            await ctx.send(embed=embed)

    @_search.command(name="usuario", aliases=["user", "member"], usage="[p]procurar usuario [name]")
    @commands.guild_only()
    async def user(self, ctx, *, user: str):
        lista = []
        for membro in ctx.guild.members:
            if SequenceMatcher(None, user, membro.name).ratio() >= 0.5:
                lista.append(f"{RightI} {membro.mention}")

        if len(lista) == 0:
            await ctx.send(embed=discord.Embed(color=0xc63939, description=f"{ctx.author.mention}: Não achei nem um usuário com este nome ou parecido."))
        else:
            filtro = "\n".join(lista)
            embed = discord.Embed(title=f"{FindUserI} Procurar - {ctx.guild.name}", description=f"{filtro}", color=0x4B0082)
            embed.set_footer(text=f"Total de usuário(s) achado(s) {len(lista)}")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(MyUtils(client))
