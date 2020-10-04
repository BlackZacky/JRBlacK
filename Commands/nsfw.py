import discord
import aiohttp
import json

from discord.ext import commands

i_nsfw = "<:18:599320214265659403>"

class NSFW(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def nekobot_request(self, imgtype: str):
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
            return await ctx.send(embed=discord.Embed(color=0xDEADBF, description=f"{i_nsfw} Eu desativei o nsfw deste canal."))
        
        await channel.edit(nsfw=True)
        await ctx.send(embed=discord.Embed(color=0xDEADBF, description=f"{i_nsfw} Eu ativei o nsfw deste canal."))

    @_nsfw.command(name="anal")
    @commands.guild_only()
    @commands.cooldown(25, 10, commands.BucketType.user)
    async def _anal(self, ctx):
        if not ctx.message.channel.is_nsfw():
            return await ctx.send(embed=discord.Embed(color=0xc63939, description='Comandos nsfw não é permitido neste canal. Ative a opção usando o comando **``.nsfw``**'))
        
        url = await self.nekobot_request('anal')

        embed = discord.Embed(title=f'{i_nsfw}Anal', color=0xDEADBF)
        embed.set_image(url=url)
        embed.set_footer(text=f'Pedido por {ctx.author.name}')
        await ctx.send(embed=embed)

    @_nsfw.command(name="buceta", aliases=["pussy"])
    @commands.guild_only()
    @commands.cooldown(25, 10, commands.BucketType.user)
    async def _pussy(self, ctx):
        if not ctx.message.channel.is_nsfw():
            return await ctx.send(embed=discord.Embed(color=0xc63939, description='Comandos nsfw não é permitido neste canal. Ative a opção usando o comando **``.nsfw``**'))

        url = await self.nekobot_request('pussy')

        embed = discord.Embed(title=f'{i_nsfw}Buceta', color=0xDEADBF)
        embed.set_image(url=url)
        embed.set_footer(text=f'Pedido por {ctx.author.name}')
        await ctx.send(embed=embed)

    @_nsfw.command(name='4k')
    @commands.guild_only()
    @commands.cooldown(25, 10, commands.BucketType.user)
    async def _4k(self, ctx):
        if not ctx.message.channel.is_nsfw():
            return await ctx.send(embed=discord.Embed(color=0xc63939, description='Comandos nsfw não é permitido neste canal. Ative a opção usando o comando **``.nsfw``**'))

        url = await self.nekobot_request('4k')

        embed = discord.Embed(title=f'{i_nsfw}4k', color=0xDEADBF)
        embed.set_image(url=url)
        embed.set_footer(text=f'Pedido por {ctx.author.name}')
        await ctx.send(embed=embed)

    @_nsfw.command(name="bunda", aliases=["ass"])
    @commands.guild_only()
    @commands.cooldown(25, 10, commands.BucketType.user)
    async def _ass(self, ctx):
        if not ctx.message.channel.is_nsfw():
            return await ctx.send(embed=discord.Embed(color=0xc63939, description='Comandos nsfw não é permitido neste canal. Ative a opção usando o comando **``.nsfw``**'))
        
        url = await self.nekobot_request('ass')

        embed = discord.Embed(title=f'{i_nsfw}Bunda', color=0xDEADBF)
        embed.set_image(url=url)
        embed.set_footer(text=f'Pedido por {ctx.author.name}')
        await ctx.send(embed=embed)

    @_nsfw.command(name="pgif", aliases=["gif"])
    @commands.guild_only()
    @commands.cooldown(25, 10, commands.BucketType.user)
    async def _pgif(self, ctx):
        if not ctx.message.channel.is_nsfw():
            return await ctx.send(embed=discord.Embed(color=0xc63939, description='Comandos nsfw não é permitido neste canal. Ative a opção usando o comando **``.nsfw``**'))
        
        url = await self.nekobot_request('pgif')

        embed = discord.Embed(title=f'{i_nsfw}PGif', color=0xDEADBF)
        embed.set_image(url=url)
        embed.set_footer(text=f'Pedido por {ctx.author.name}')
        await ctx.send(embed=embed)

    @_nsfw.command(name="coxa", aliases=["thigh"])
    @commands.guild_only()
    @commands.cooldown(25, 10, commands.BucketType.user)
    async def _thigh(self, ctx):
        if not ctx.message.channel.is_nsfw():
            return await ctx.send(embed=discord.Embed(color=0xc63939, description='Comandos nsfw não é permitido neste canal. Ative a opção usando o comando **``.nsfw``**'))
        
        url = await self.nekobot_request('thigh')

        embed = discord.Embed(title=f'{i_nsfw}Coxa', color=0xDEADBF)
        embed.set_image(url=url)
        embed.set_footer(text=f'Pedido por {ctx.author.name}')
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(NSFW(client))
