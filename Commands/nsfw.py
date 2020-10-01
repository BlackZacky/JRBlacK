import discord
import aiohttp
import json
import requests

from discord.ext import commands

nsfwI = "<:18:599320214265659403>"

class NSFW(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def nekobot(self, imgtype: str):
        async with aiohttp.ClientSession() as http:
            async with http.get("https://nekobot.xyz/api/image?type=%s" % imgtype) as res:
                res = await res.json()
        return res["message"]

    @commands.group(name="nsfw", aliases=["sex", "sexy", "porno", "porns"], usage="[p]nsfw [sub comando]")
    @commands.guild_only()
    @commands.bot_has_permissions(manage_channels=True)
    @commands.has_permissions(manage_channels=True)
    async def _nsfw(self, ctx, channel: discord.TextChannel=None):
        if channel is None:
            channel = ctx.message.channel
            
        if channel.is_nsfw():
            await channel.edit(nsfw=False)
            return await ctx.send(embed=discord.Embed(color=0xDEADBF, description=f"{nsfwI} Eu desativei o nsfw deste canal."))
        
        await channel.edit(nsfw=True)
        await ctx.send(embed=discord.Embed(color=0xDEADBF, description=f"{nsfwI} Eu ativei o nsfw deste canal."))

    @_nsfw.command(name="anal")
    @commands.guild_only()
    @commands.cooldown(25, 10, commands.BucketType.user)
    async def _anal(self, ctx):
        if not ctx.message.channel.is_nsfw():
            return await ctx.send(embed=discord.Embed(color=0xc63939, description='Comandos nsfw não é permitido neste canal. Ative a opção usando o comando **``.nsfw``**'))
        
        await ctx.send(embed=discord.Embed(title=f'{nsfwI}Anal', color=0xDEADBF).set_image(url=await self.nekobot('anal')).set_footer(text=f'Pedido por {ctx.author.name}'))

    @_nsfw.command(name="pussy", aliases=["buceta"])
    @commands.guild_only()
    @commands.cooldown(25, 10, commands.BucketType.user)
    async def _pussy(self, ctx):
        if not ctx.message.channel.is_nsfw():
            return await ctx.send(embed=discord.Embed(color=0xc63939, description='Comandos nsfw não é permitido neste canal. Ative a opção usando o comando **``.nsfw``**'))

        await ctx.send(embed=discord.Embed(title=f'{nsfwI}Buceta', color=0xDEADBF).set_image(url=await self.nekobot('pussy')).set_footer(text=f'Pedido por {ctx.author.name}'))

    @_nsfw.command(name='4k')
    @commands.guild_only()
    @commands.cooldown(25, 10, commands.BucketType.user)
    async def _4k(self, ctx):
        if not ctx.message.channel.is_nsfw():
            return await ctx.send(embed=discord.Embed(color=0xc63939, description='Comandos nsfw não é permitido neste canal. Ative a opção usando o comando **``.nsfw``**'))
        
        await ctx.send(embed=discord.Embed(title=f'{nsfwI}4k', color=0xDEADBF).set_image(url=await self.nekobot('4k')).set_footer(text=f'Pedido por {ctx.author.name}'))

    @_nsfw.command(name="ass", aliases=["bunda"])
    @commands.guild_only()
    @commands.cooldown(25, 10, commands.BucketType.user)
    async def _ass(self, ctx):
        if not ctx.message.channel.is_nsfw():
            return await ctx.send(embed=discord.Embed(color=0xc63939, description='Comandos nsfw não é permitido neste canal. Ative a opção usando o comando **``.nsfw``**'))
        
        await ctx.send(embed=discord.Embed(title=f'{nsfwI}Bunda', color=0xDEADBF).set_image(url=await self.nekobot('ass')).set_footer(text=f'Pedido por {ctx.author.name}'))

    @_nsfw.command(name="pgif")
    @commands.guild_only()
    @commands.cooldown(25, 10, commands.BucketType.user)
    async def _pgif(self, ctx):
        if not ctx.message.channel.is_nsfw():
            return await ctx.send(embed=discord.Embed(color=0xc63939, description='Comandos nsfw não é permitido neste canal. Ative a opção usando o comando **``.nsfw``**'))
        
        await ctx.send(embed=discord.Embed(title=f'{nsfwI}PGif', color=0xDEADBF).set_image(url=await self.nekobot('pgif')).set_footer(text=f'Pedido por {ctx.author.name}'))

    @_nsfw.command(name="thigh", aliases=["coxa"])
    @commands.guild_only()
    @commands.cooldown(25, 10, commands.BucketType.user)
    async def _thigh(self, ctx):
        if not ctx.message.channel.is_nsfw():
            return await ctx.send(embed=discord.Embed(color=0xc63939, description='Comandos nsfw não é permitido neste canal. Ative a opção usando o comando **``.nsfw``**'))
        
        await ctx.send(embed=discord.Embed(title=f'{nsfwI}Coxa', color=0xDEADBF).set_image(url=await self.nekobot('thigh')).set_footer(text=f'Pedido por {ctx.author.name}'))

def setup(client):
    client.add_cog(NSFW(client))
