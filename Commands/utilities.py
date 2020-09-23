from difflib import SequenceMatcher
from discord.ext import commands
from Database import *

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

    async def sub_commands(self, ctx, command):
        lista = []
        for x in self.client.get_command(command).all_commands:
            if self.client.get_command(f'{command} {x}').name is x:
                lista.append(x)

        x = "".join(lista)
        if len(lista) > 1:
            x = " | ".join(lista)

        return await ctx.send(f"""```asciidoc
[Comando {command}]
  Modo de uso    :: {self.client.get_command(command).usage}
  Sub Comando(s) :: {x}
```""")

    @commands.group(name="procurar", aliases=["find", "search"], usage="[p]procurar [sub comando]")
    async def _search(self, ctx):
        if ctx.invoked_subcommand is None:
            if self.guild.get_whitelist(ctx.guild.id) == ctx.channel.id or self.guild.get_whitelist(ctx.guild.id) == 0:
                return await self.sub_commands(ctx, ctx.command.name)
            else:
                return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention}, você não pode executar comandos nesse chat.", color=0xef0027), delete_after=15)

    @_search.command(name="comando", aliases=["commands", "cog", "command", "comandos"], usage="[p]procurar comando [name]")
    async def command(self, ctx, command: str):
        if self.guild.get_whitelist(ctx.guild.id) == ctx.channel.id or self.guild.get_whitelist(ctx.guild.id) == 0:
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
        else:
            return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention}, você não pode executar comandos nesse chat.", color=0xef0027), delete_after=15)

    @_search.command(name="usuario", aliases=["user", "member"], usage="[p]procurar usuario [name]")
    async def user(self, ctx, *, user: str):
        if self.guild.get_whitelist(ctx.guild.id) == ctx.channel.id or self.guild.get_whitelist(ctx.guild.id) == 0:
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
        else:
            return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention}, você não pode executar comandos nesse chat.", color=0xef0027), delete_after=15)

def setup(client):
    client.add_cog(MyUtils(client))
