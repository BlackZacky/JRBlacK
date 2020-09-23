from discord.ext import commands
from Database import *

import discord

IdentityI = "<:identity:571169485831012393>"
TitleI    = "<:title:571170332497412097>"
ResumeI   = "<:resume:571394962894225408>"
HintI     = "<:hint:571396019322093580>"

class MySuggestions(commands.Cog, name="Sugestão"):
    def __init__(self, client):
        self.client = client
        self.check  = database.check()
        self.guild  = database.guild()

    @commands.command()
    @commands.guild_only()
    async def sugestão(self, ctx):
        if self.guild.get_whitelist(ctx.guild.id) == ctx.channel.id or self.guild.get_whitelist(ctx.guild.id) == 0:

            if self.check.guild(ctx.guild.id) is False:
                return await ctx.send(embed=discord.Embed(description=f"Me parece que seu servidor não está configurado na minha database. COMMAND: @{self.bot.user.name}!?", color=0xef0027))
            
            ChannelSug = self.guild.get_autoReact(ctx.guild.id)
            if ChannelSug == 0:
                return await ctx.send(embed=discord.Embed(description="Comando de sugestão está desativado.", color=0xef0027))

            def checker(message):
                return message.author == ctx.author
            while True:
                try:
                    author1 = await ctx.author.send(embed=discord.Embed(description="Qual o nome da sua sugestão ?! (Mín: 4/ Max: 20) (3 Min)", color=0x444444))
                except:
                    return await ctx.send(embed=discord.Embed(description="Seu privado está bloqueado.", color=0xef0027))
                try:
                    Name0 = await self.client.wait_for("message", check=checker, timeout=180)
                except:
                    return await author1.edit(embed=discord.Embed(description="Seu tempo acabou de 3 minutos acabou!", color=0xef0027))

                if len(Name0.content) > 20:
                    return await ctx.author.send(embed=discord.Embed(description="Máximo de letras é 20!", color=0xef0027))

                elif len(Name0.content) >= 4:
                    sugestão1 = await ctx.author.send(embed=discord.Embed(description="Qual sua sugestão ?? (Mín: 10) (5 Min)", color=0x444444))
                    try:
                        Description0 = await self.client.wait_for("message", check=checker, timeout=300)
                    except:
                        return await sugestão1.edit(embed=discord.Embed(description="Seu tempo acabou de 5 minutos acabou!", color=0xef0027))
                    
                    if len(Description0.content) <= 10:
                        return await ctx.author.send(embed=discord.Embed(description="Mínimo de letras é 10!", color=0xef0027))
                    
                    embed = discord.Embed(title=f"{HintI}Sugestão - {ctx.guild.name}", color=0x444444)
                    embed.add_field(name=f"{IdentityI}Por:", value=f"```{ctx.author.name}```", inline=True)
                    embed.add_field(name=f"{TitleI}Título:", value=f"```{Name0.content}```", inline=False)
                    embed.add_field(name=f"{ResumeI}Descrição:", value=f"```{Description0.content}```", inline=False)

                    await self.client.get_channel(ChannelSug).send(embed=embed)

                    await ctx.author.send(embed=discord.Embed(description="Obrigado pela sugestão, ela foi adiconada com sucesso.", color=0x444444))

                elif len(NameSug.content) <= 4:
                    return await ctx.author.send(embed=discord.Embed(description="Mínimo de letras é 4!", color=0x00ef5b))

                    await author1.delete()
                    await sugestão1.delete()
                break

def setup(bot):
    bot.add_cog(MySuggestions(bot))