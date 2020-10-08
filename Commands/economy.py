from Commands.Utils.icons import getIcon
from discord.ext import commands
from datetime import datetime
from Database import *
from . import sub_commands

import discord
import random

i_receiver  = getIcon("Receiver")
i_transfer  = getIcon("Transfer")
i_extract   = getIcon("Extract")
i_deposit   = getIcon("Deposit")
i_wallet    = getIcon("Wallet")
i_money     = getIcon("Money")
i_name      = getIcon("Name")
i_bank      = getIcon("Bank")
i_rank      = getIcon("Rank")
i_atm       = getIcon("Atm")
i_id        = getIcon("ID")

"""class economy(commands.Cog):
    def __init__(self, bot):
        self.client = bot
        self.Guild    = database.Guild()
        self.GuildGet = database.GuildGet()
        self.User     = database.User()
        self.user. = database.UserPost()
        self.user.  = database.UserGet()

    async def withdrawMoney(self, guild, member, money):

    async def depositMoney(self, guild, member, money):"""

class MyBank(commands.Cog, name="Banco"):
    def __init__(self, client):
        self.client = client
        self.check = database.check()
        self.guild = database.guild()
        self.user  = database.user()

    @commands.group(name="banco", aliases=["bank", "economy"], usage="[p]banco [sub command]")
    @commands.guild_only()
    async def _bank(self, ctx):
        if self.guild.get_system_economy(ctx.guild.id) == 'True':
            if not self.check.user(ctx.guild.id, ctx.author.id):
                self.user.create(ctx.guild.id, ctx.author.id)

        if ctx.invoked_subcommand is None:
            return await sub_commands(self.client, ctx, ctx.command.name)

    @_bank.command(aliases=['diariamente', 'salario'], usage="[p]banco daily")
    @commands.guild_only()
    @commands.cooldown(1, 54000, commands.BucketType.member)
    async def daily(self, ctx):
        if self.guild.get_system_economy(ctx.guild.id) == 'False':
            return await ctx.send(embed=discord.Embed(description=f"{i_bank} Sistema de economia está desativado neste grupo.", color=0xef0027).set_footer(text="Para tivar use o comando: [p]set economy"))

        valores = '1234567890'
        d = (f'{random.choice(valores)}{random.choice(valores)}{random.choice(valores)}')

        self.user.post_money_hand(ctx.guild.id, ctx.author.id, int(d))
        await ctx.send(embed=discord.Embed(color=0x444444, description=f"**{ctx.author.mention}: Reclamou seu Daily Reward no valor de: `${d}`.**"))

    @_bank.command(name="depositar", alises=["deposit"], usage="[p]banco depositar [valor]")
    @commands.cooldown(1, 900, commands.BucketType.member)
    async def deposit(self, ctx, Money:int=None):
        if self.guild.get_whitelist(ctx.guild.id) == ctx.channel.id or self.guild.get_whitelist(ctx.guild.id) == 0:
            if self.guild.get_system_economy(ctx.guild.id) == 'False':
                return await ctx.send(embed=discord.Embed(description=f"{i_bank} Sistema de economia está desativado neste grupo.", color=0xef0027).set_footer(text="Para tivar use o comando: [p]set economy"))

            if Money <= 0:
                return await ctx.send(embed=discord.Embed(description=f"{i_bank} Valor não aceito.", color=0xef0027))

            Hand = self.user.get_money_hand(ctx.guild.id, ctx.author.id)

            #newMoneyPorcentage = Money - (Money * 10 / 100)

            if Hand >= Money:
                self.user.post_money_hand(ctx.guild.id, ctx.author.id, -Money)
                self.user.post_money_bank(ctx.guild.id, ctx.author.id, Money)

                embed = discord.Embed(title=f"{i_deposit} Banco - {ctx.guild.name}", color=0x00ef5b, timestamp=datetime.utcnow())                
                embed.add_field(name=f"{i_name}Nome:", value=f'**```{ctx.author.name}```**')
                embed.add_field(name=f"{i_id}ID:", value=f'**```{ctx.author.id}```**')
                embed.add_field(name=f"{i_bank}Banco:", value=f'**```${Money}```**', inline=False)

            elif Hand < Money:
                embed = discord.Embed(title=f"{i_deposit} Banco - {ctx.guild.name}", color=0xef0027, timestamp=datetime.utcnow())                
                embed.add_field(name=f"{i_name}Nome:", value=f'**```{ctx.author.name}```**')
                embed.add_field(name=f"{i_id}ID:", value=f'**```{ctx.author.id}```**')
                embed.add_field(name=f"{i_bank}Banco:", value="**```Abstinência do valor requisitado!```**", inline=False)

            embed.set_footer(text="Dinheiro não real!")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention}, você não pode executar comandos nesse chat.", color=0xef0027), delete_after=15)

    @_bank.command(name="sacar", alises=["draw"], usage="[p]banco sacar [valor]")
    @commands.guild_only()
    async def draw(self, ctx, Money:int=None):
        if self.guild.get_whitelist(ctx.guild.id) == ctx.channel.id or self.guild.get_whitelist(ctx.guild.id) == 0:
            if self.guild.get_system_economy(ctx.guild.id) == 'False':
                return await ctx.send(embed=discord.Embed(description=f"{i_bank} Sistema de economia está desativado neste grupo.", color=0xef0027).set_footer(text="Para tivar use o comando: [p]set economy"))

            if Money < 0:
                return await ctx.send(embed=discord.Embed(description=f"{i_bank} Valor não aceito.", color=0xef0027))

            Bank = self.user.get_money_bank(ctx.guild.id, ctx.author.id)

            if Bank >= Money:
                self.user.post_money_hand(ctx.guild.id, ctx.author.id, Money)
                self.user.post_money_bank(ctx.guild.id, ctx.author.id, -Money)

                embed = discord.Embed(title=f"{i_atm} Banco - {ctx.guild.name}", color=0x00ef5b, timestamp=datetime.utcnow())
                embed.add_field(name=f"{i_name}Nome:", value=f'**```{ctx.author.name}```**')
                embed.add_field(name=f"{i_id}ID:", value=f'**```{ctx.author.id}```**')
                embed.add_field(name=f"{i_bank}Banco:", value=f'**```${Money}```**', inline=False)

            elif Bank < Money:
                embed = discord.Embed(title=f"{i_atm} Banco - {ctx.guild.name}", color=0xef0027, timestamp=datetime.utcnow())
                embed.add_field(name=f"{i_name}Nome:", value=f'**```{ctx.author.name}```**')
                embed.add_field(name=f"{i_id}ID:", value=f'**```{ctx.author.id}```**')
                embed.add_field(name=f"{i_bank}Banco:", value="**```Abstinência do valor requisitado!```**", inline=False)

            embed.set_footer(text="Dinheiro não real!")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention}, você não pode executar comandos nesse chat.", color=0xef0027), delete_after=15)

    @_bank.command(name="transferir", aliases=["transfer"], usage="[p]banco transferir [membro] [valor]")
    @commands.guild_only()
    async def transfer(self, ctx, Member:discord.Member=None, Money:int=None):
        if self.guild.get_whitelist(ctx.guild.id) == ctx.channel.id or self.guild.get_whitelist(ctx.guild.id) == 0:
            if self.guild.get_system_economy(ctx.guild.id) == 'False':
                return await ctx.send(embed=discord.Embed(description=f"{i_bank} Sistema de economia está desativado neste grupo.", color=0xef0027).set_footer(text="Para tivar use o comando: [p]set economy"))

            if Member is None:
                return await ctx.send(embed=discord.Embed(description=f"{i_bank} Membro não informado.", color=0xef0027))
            if Money is None:
                return await ctx.send(embed=discord.Embed(description=f"{i_bank} Valor não informado.", color=0xef0027))
            if Money < 0:
                return await ctx.send(embed=discord.Embed(description=f"{i_bank} Valor não aceito.", color=0xef0027))

            Bank = self.user.get_money_bank(ctx.guild.id, ctx.author.id)

            if Bank >= Money:
                self.user.post_money_bank(ctx.guild.id, Member.id, Money)
                self.user.post_money_bank(ctx.guild.id, ctx.author.id, -Money)

                embed = discord.Embed(title=f"{i_transfer} Banco - {ctx.guild.name}", color=0x00ef5b, timestamp=datetime.utcnow())
                embed.add_field(name=f"{i_name}Nome:", value=f'**```{ctx.author.name}```**')
                embed.add_field(name=f"{i_id}ID:", value=f'**```{ctx.author.id}```**')
                embed.add_field(name=f"{i_receiver}Destinatário:", value=f"**```{Member.name}```**")
                embed.add_field(name=f"{i_bank}Banco:", value=f'**```${Money}```**', inline=False)
                embed.set_footer(text="Transferencia aprovada!")
            elif Bank < Money:
                embed = discord.Embed(title=f"{i_transfer} Banco - {ctx.guild.name}", color=0xef0027, timestamp=datetime.utcnow())
                embed.add_field(name=f"{i_name}Nome:", value=f'**```{ctx.author.name}```**')
                embed.add_field(name=f"{i_id}ID:", value=f'**```{ctx.author.id}```**')
                embed.add_field(name=f"{i_receiver}Destinatário:", value=f"**```{Member.name}```**")
                embed.add_field(name=f"{i_bank}Banco:", value="**```Abstinência do valor requisitado!```**", inline=False)
                embed.set_footer(text="Transferencia reprovada!")

            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention}, você não pode executar comandos nesse chat.", color=0xef0027), delete_after=15)
    
    @_bank.command(name="extrato", aliases=["extract"], usage="[p]banco extrato")
    @commands.guild_only()
    async def extract(self, ctx):
        if self.guild.get_whitelist(ctx.guild.id) == ctx.channel.id or self.guild.get_whitelist(ctx.guild.id) == 0:
            if self.guild.get_system_economy(ctx.guild.id) == 'False':
                return await ctx.send(embed=discord.Embed(description=f"{i_bank} Sistema de economia está desativado neste grupo.", color=0xef0027).set_footer(text="Para tivar use o comando: [p]set economy"))

            Hand = self.user.get_money_hand(ctx.guild.id, ctx.author.id)
            Bank = self.user.get_money_bank(ctx.guild.id, ctx.author.id)

            embed = discord.Embed(title=f"{i_extract} Banco - {ctx.guild.name}", color=0x00ef5b, timestamp=datetime.utcnow())
            embed.add_field(name=f"{i_name}Nome:", value=f'**```{ctx.author.name}```**')
            embed.add_field(name=f"{i_id}ID:", value=f'**```{ctx.author.id}```**')
            embed.add_field(name=f"{i_bank}Banco:", value=f'**```${Bank}```**', inline=False)
            embed.add_field(name=f"{i_wallet}Carteira:", value=f'**```${Hand}```**', inline=False)
            embed.add_field(name=f"{i_money}Total:", value=f'**```${int(Bank)+int(Hand)}```**', inline=False)
            embed.set_footer(text="Dinheiro não real!")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention}, você não pode executar comandos nesse chat.", color=0xef0027), delete_after=15)

    @_bank.command(name="classificação", aliases=["rank","ranking"], usage="[p]banco rank")
    @commands.guild_only()
    async def ranking(self, ctx):
        if self.guild.get_whitelist(ctx.guild.id) == ctx.channel.id or self.guild.get_whitelist(ctx.guild.id) == 0:
            if self.guild.get_system_economy(ctx.guild.id) == 'False':
                return await ctx.send(embed=discord.Embed(description=f"{i_bank} Sistema de economia está desativado neste grupo.", color=0xef0027).set_footer(text="Para tivar use o comando: [p]set economy"))

            await ctx.send(embed=discord.Embed(title=f"{i_rank}Banco - {ctx.guild.name}", color=0x444444, description=self.user.get_bank_rank(ctx.guild.id, ctx.author.id)))
        else:
            return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention}, você não pode executar comandos nesse chat.", color=0xef0027), delete_after=15)

    @daily.error
    async def daily_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            min, sec = divmod(error.retry_after, 60)
            h, min = divmod(min, 60)
            if min == 0.0 and h == 0:
                await ctx.send(embed=discord.Embed(color=0xef0027, description=f"**{ctx.author.mention} : Espere por ``{round(sec)}`` segundos.**"))
            else:
                await ctx.send(embed=discord.Embed(color=0xef0027, description=f"**{ctx.author.mention} : Só poderá pegar outro Daily Reward em ``{round(h)}`` hora(s) e ``{round(min)}`` minuto(s).**"))

    @deposit.error
    async def deposit_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            min, sec = divmod(error.retry_after, 60)
            h, min = divmod(min, 60)

            if min == 0.0 and h == 0:
                await ctx.send(embed=discord.Embed(color=0xef0027, description=f"**{ctx.author.mention} : Espere por ``{round(sec)}`` segundos.**"))
            else:
                await ctx.send(embed=discord.Embed(color=0xef0027, description=f"**{ctx.author.mention} : Só podera depositar em ``{round(h)}`` hora(s) e ``{round(min)}`` minuto(s).**"))

def setup(client):
    client.add_cog(MyBank(client))