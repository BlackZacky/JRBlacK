from discord.ext import commands
from Database import database

from Commands.Utils.icons import getIcon
from Commands.Utils import checks

import discord

IdentityI = getIcon("Identity")
LanguageI = getIcon("Language")
StorageI  = getIcon("Storage")
TitleI    = getIcon("Name")
WebsiteI  = getIcon("Website")
CalendarI = getIcon("Calendar")
DesignI   = getIcon("Design")
HddI      = getIcon("HD")
ImacI     = getIcon("Imac")

class MyHardDisk(commands.Cog, name="Disco Rigido"):
    def __init__(self, client):
        self.client = client
        self.guild  = database.guild()
        self.check  = database.check()

    @commands.command()
    @commands.guild_only()
    async def harddisk(self, ctx):
        ChannelHard = self.guild.get_harddisk(ctx.guild.id)
        if ChannelHard == 0:
            return await ctx.send(embed=discord.Embed(description="Comando HardDisk está desativado.", color=0xef0027))

        def checker(message):
            return message.author == ctx.author and message.author.dm_channel == message.channel

        try:
            author0 = await ctx.author.send(embed=discord.Embed(description="Qual título do curso/apostila ? (Min: 3) (1/7)", color=0x444444))
        except:
            return await ctx.send(embed=discord.Embed(description="Seu privado está desativado.", color=0xef0027))
        try:
            titulo = await self.client.wait_for("message", check=checker, timeout=180)
        except:
            return await ctx.author.send(embed=discord.Embed(description="Seu tempo acabou! :(", color=0xef0027))

        try:
            editora0 = await ctx.author.send(embed=discord.Embed(description="Qual editora ? (Min: 3) (2/7)", color=0x444444))
            editora = await self.client.wait_for("message", check=checker, timeout=180)
        except:
            return await ctx.author.send(embed=discord.Embed(description="Seu tempo acabou! :(", color=0xef0027))

        try:
            genero0 = await ctx.author.send(embed=discord.Embed(description="Qual gênero ? (Min: 3) (3/7)", color=0x444444))
            genero = await self.client.wait_for("message", check=checker, timeout=180)
        except:
            return await ctx.author.send(embed=discord.Embed(description="Seu tempo acabou! :(", color=0xef0027))  

        try:
            ano0 = await ctx.author.send(embed=discord.Embed(description="Qual ano do curso/apostila ? (Min: 3) (4/7)", color=0x444444))
            ano = await self.client.wait_for("message", check=checker, timeout=180)
        except:
            return await ctx.author.send(embed=discord.Embed(description="Seu tempo acabou! :(", color=0xef0027))  

        try:
            tamanho0 = await ctx.author.send(embed=discord.Embed(description="Qual tamanho do arquivo ? (Min: 3) (5/7)", color=0x444444))
            tamanho = await self.client.wait_for("message", check=checker, timeout=180)
        except:
            return await ctx.author.send(embed=discord.Embed(description="Seu tempo acabou! :(", color=0xef0027))

        try:
            idioma0 = await ctx.author.send(embed=discord.Embed(description="Qual o idioma do curso/apostila ? (Min: 3) (6/7)", color=0x444444))
            idioma = await self.client.wait_for("message", check=checker, timeout=180)
        except:
            return await ctx.author.send(embed=discord.Embed(description="Seu tempo acabou! :(", color=0xef0027))

        try:
            link0 = await ctx.author.send(embed=discord.Embed(description="Qual link para download ?? (Min: 3) (7/7)", color=0x444444))
            link = await self.client.wait_for("message", check=checker, timeout=180)
        except:
            return await ctx.author.send(embed=discord.Embed(description="Seu tempo acabou! :(", color=0xef0027))

        embed = discord.Embed(title=f"{HddI}HardDisk - {ctx.guild.name}", color=0x444444)

        embed.add_field(name=f"{IdentityI}Por:", value=f"```{ctx.author.name}```", inline=True)
        embed.add_field(name=f"{DesignI}Editora:", value=f"```{editora.content}```", inline=True)
        embed.add_field(name=f"{ImacI}Gênero:", value=f"```{genero.content}```", inline=True)
        embed.add_field(name=f"{LanguageI}Idioma:", value=f"```{idioma.content}```", inline=True)
        embed.add_field(name=f"{CalendarI}Ano:", value=f"```{ano.content}```", inline=True)
        embed.add_field(name=f"{StorageI}Tamanho:", value=f"```{tamanho.content}```", inline=True)
        embed.add_field(name=f"{TitleI}Título:", value=f"```{titulo.content}```", inline=False)

        if "http://" in link.content or "https://" in link.content:
            embed.add_field(name=f"{WebsiteI}Download:", value=f"```{link.content}```\nMobile: [**`link`**]({link.content})", inline=False)
        else:
            embed.add_field(name=f"{WebsiteI}Download:", value=f"```{link.content}```", inline=False)

        await self.client.get_channel(ChannelHard).send(embed=embed)

        await ctx.author.send(embed=discord.Embed(description="Curso/Apostila foi adicionado com sucesso.", color=0x00ef5b))

    @commands.command()
    @commands.guild_only()
    async def harddisk2(self, ctx):
        ChannelHard = self.guild.get_harddisk_2(ctx.guild.id)
        if ChannelHard == 0:
            return await ctx.send(embed=discord.Embed(description="Comando HardDisk está desativado.", color=0xef0027))

        def checker(message):
            return message.author == ctx.author and message.author.dm_channel == message.channel

        try:
            author0 = await ctx.author.send(embed=discord.Embed(description="Qual título do curso/apostila ? (Min: 3) (1/7)", color=0x444444))
        except:
            return await ctx.send(embed=discord.Embed(description="Seu privado está desativado.", color=0xef0027))
        try:
            titulo = await self.client.wait_for("message", check=checker, timeout=180)
        except:
            return await ctx.author.send(embed=discord.Embed(description="Seu tempo acabou! :(", color=0xef0027))

        try:
            editora0 = await ctx.author.send(embed=discord.Embed(description="Qual editora ? (Min: 3) (2/7)", color=0x444444))
            editora = await self.client.wait_for("message", check=checker, timeout=180)
        except:
            return await ctx.author.send(embed=discord.Embed(description="Seu tempo acabou! :(", color=0xef0027))

        try:
            genero0 = await ctx.author.send(embed=discord.Embed(description="Qual gênero ? (Min: 3) (3/7)", color=0x444444))
            genero = await self.client.wait_for("message", check=checker, timeout=180)
        except:
            return await ctx.author.send(embed=discord.Embed(description="Seu tempo acabou! :(", color=0xef0027))  

        try:
            ano0 = await ctx.author.send(embed=discord.Embed(description="Qual ano do curso/apostila ? (Min: 3) (4/7)", color=0x444444))
            ano = await self.client.wait_for("message", check=checker, timeout=180)
        except:
            return await ctx.author.send(embed=discord.Embed(description="Seu tempo acabou! :(", color=0xef0027))  

        try:
            tamanho0 = await ctx.author.send(embed=discord.Embed(description="Qual tamanho do arquivo ? (Min: 3) (5/7)", color=0x444444))
            tamanho = await self.client.wait_for("message", check=checker, timeout=180)
        except:
            return await ctx.author.send(embed=discord.Embed(description="Seu tempo acabou! :(", color=0xef0027))

        try:
            idioma0 = await ctx.author.send(embed=discord.Embed(description="Qual o idioma do curso/apostila ? (Min: 3) (6/7)", color=0x444444))
            idioma = await self.client.wait_for("message", check=checker, timeout=180)
        except:
            return await ctx.author.send(embed=discord.Embed(description="Seu tempo acabou! :(", color=0xef0027))

        try:
            link0 = await ctx.author.send(embed=discord.Embed(description="Qual link para download ?? (Min: 3) (7/7)", color=0x444444))
            link = await self.client.wait_for("message", check=checker, timeout=180)
        except:
            return await ctx.author.send(embed=discord.Embed(description="Seu tempo acabou! :(", color=0xef0027))

        embed = discord.Embed(title=f"{HddI}HardDisk - {ctx.guild.name}", color=0x444444)

        embed.add_field(name=f"{IdentityI}Por:", value=f"```{ctx.author.name}```", inline=True)
        embed.add_field(name=f"{DesignI}Editora:", value=f"```{editora.content}```", inline=True)
        embed.add_field(name=f"{ImacI}Gênero:", value=f"```{genero.content}```", inline=True)
        embed.add_field(name=f"{LanguageI}Idioma:", value=f"```{idioma.content}```", inline=True)
        embed.add_field(name=f"{CalendarI}Ano:", value=f"```{ano.content}```", inline=True)
        embed.add_field(name=f"{StorageI}Tamanho:", value=f"```{tamanho.content}```", inline=True)
        embed.add_field(name=f"{TitleI}Título:", value=f"```{titulo.content}```", inline=False)

        if "http://" in link.content or "https://" in link.content:
            embed.add_field(name=f"{WebsiteI}Download:", value=f"```{link.content}```\nMobile: [**`link`**]({link.content})", inline=False)
        else:
            embed.add_field(name=f"{WebsiteI}Download:", value=f"```{link.content}```", inline=False)

        await self.client.get_channel(ChannelHard).send(embed=embed)

        await ctx.author.send(embed=discord.Embed(description="Curso/Apostila foi adicionado com sucesso.", color=0x00ef5b))

    @commands.command()
    @commands.guild_only()
    async def harddisk3(self, ctx):
        ChannelHard = self.guild.get_harddisk_3(ctx.guild.id)
        if ChannelHard == 0:
            return await ctx.send(embed=discord.Embed(description="Comando HardDisk está desativado.", color=0xef0027))

        def checker(message):
            return message.author == ctx.author and message.author.dm_channel == message.channel

        try:
            author0 = await ctx.author.send(embed=discord.Embed(description="Qual título do curso/apostila ? (Min: 3) (1/7)", color=0x444444))
        except:
            return await ctx.send(embed=discord.Embed(description="Seu privado está desativado.", color=0xef0027))
        try:
            titulo = await self.client.wait_for("message", check=checker, timeout=180)
        except:
            return await ctx.author.send(embed=discord.Embed(description="Seu tempo acabou! :(", color=0xef0027))

        try:
            editora0 = await ctx.author.send(embed=discord.Embed(description="Qual editora ? (Min: 3) (2/7)", color=0x444444))
            editora = await self.client.wait_for("message", check=checker, timeout=180)
        except:
            return await ctx.author.send(embed=discord.Embed(description="Seu tempo acabou! :(", color=0xef0027))

        try:
            genero0 = await ctx.author.send(embed=discord.Embed(description="Qual gênero ? (Min: 3) (3/7)", color=0x444444))
            genero = await self.client.wait_for("message", check=checker, timeout=180)
        except:
            return await ctx.author.send(embed=discord.Embed(description="Seu tempo acabou! :(", color=0xef0027))  

        try:
            ano0 = await ctx.author.send(embed=discord.Embed(description="Qual ano do curso/apostila ? (Min: 3) (4/7)", color=0x444444))
            ano = await self.client.wait_for("message", check=checker, timeout=180)
        except:
            return await ctx.author.send(embed=discord.Embed(description="Seu tempo acabou! :(", color=0xef0027))  

        try:
            tamanho0 = await ctx.author.send(embed=discord.Embed(description="Qual tamanho do arquivo ? (Min: 3) (5/7)", color=0x444444))
            tamanho = await self.client.wait_for("message", check=checker, timeout=180)
        except:
            return await ctx.author.send(embed=discord.Embed(description="Seu tempo acabou! :(", color=0xef0027))

        try:
            idioma0 = await ctx.author.send(embed=discord.Embed(description="Qual o idioma do curso/apostila ? (Min: 3) (6/7)", color=0x444444))
            idioma = await self.client.wait_for("message", check=checker, timeout=180)
        except:
            return await ctx.author.send(embed=discord.Embed(description="Seu tempo acabou! :(", color=0xef0027))

        try:
            link0 = await ctx.author.send(embed=discord.Embed(description="Qual link para download ?? (Min: 3) (7/7)", color=0x444444))
            link = await self.client.wait_for("message", check=checker, timeout=180)
        except:
            return await ctx.author.send(embed=discord.Embed(description="Seu tempo acabou! :(", color=0xef0027))

        embed = discord.Embed(title=f"{HddI}HardDisk - {ctx.guild.name}", color=0x444444)

        embed.add_field(name=f"{IdentityI}Por:", value=f"```{ctx.author.name}```", inline=True)
        embed.add_field(name=f"{DesignI}Editora:", value=f"```{editora.content}```", inline=True)
        embed.add_field(name=f"{ImacI}Gênero:", value=f"```{genero.content}```", inline=True)
        embed.add_field(name=f"{LanguageI}Idioma:", value=f"```{idioma.content}```", inline=True)
        embed.add_field(name=f"{CalendarI}Ano:", value=f"```{ano.content}```", inline=True)
        embed.add_field(name=f"{StorageI}Tamanho:", value=f"```{tamanho.content}```", inline=True)
        embed.add_field(name=f"{TitleI}Título:", value=f"```{titulo.content}```", inline=False)

        if "http://" in link.content or "https://" in link.content:
            embed.add_field(name=f"{WebsiteI}Download:", value=f"```{link.content}```\nMobile: [**`link`**]({link.content})", inline=False)
        else:
            embed.add_field(name=f"{WebsiteI}Download:", value=f"```{link.content}```", inline=False)

        await self.client.get_channel(ChannelHard).send(embed=embed)

        await ctx.author.send(embed=discord.Embed(description="Curso/Apostila foi adicionado com sucesso.", color=0x00ef5b))

def setup(client):
    client.add_cog(MyHardDisk(client))