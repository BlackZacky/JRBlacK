from random import randint, choice, randrange
from discord.ext import commands
from Database import database
from Commands.Utils.icons import getIcon

import discord

FrankI    = getIcon("Frank")
JackI     = getIcon("Jack")
ConfettiI = getIcon("Conffeti")
ThrillerI = getIcon("Thriller")
CasanikI  = getIcon("Casanik")
GhostI    = getIcon("Ghost")
BankI     = getIcon("Bank")
WinI      = getIcon("Win")

class MyFunny(commands.Cog, name="Diversão"):
    def __init__(self, client):
        self.client   = client
        self.guild    = database.guild()
        self.user     = database.user()
        self.check    = database.check()
        self.bot      = database.bot()
        self.casanik_icons = [FrankI, GhostI, ThrillerI, JackI]

    @commands.command(aliases=["assaltar"])
    async def roubar(self, ctx, member:discord.Member=None):
        if member is None:
            return await ctx.send(embed=discord.Embed(description=f"Você precisa mencionar quem deseja roubar...", color=0xef0027))
        if member.id == ctx.author.id:
            return await ctx.send(embed=discord.Embed(description=f"Você não pode assaltar a si mesmo.", color=0xef0027))
        if member.id == self.client.user.id:
            return await ctx.send(embed=discord.Embed(description=f"Você não pode assaltar me assaltar.", color=0xef0027))
        if len(self.user.get_inventory_weapon(ctx.guild.id, ctx.author.id)) <= 0:
            return await ctx.send(embed=discord.Embed(description=f"Você não possui uma arma para poder estar assaltando...", color=0xef0027))
        if self.user.get_money_hand(ctx.guild.id, member.id) <= 0:
            return await ctx.send(embed=discord.Embed(description=f"Kkkkk infelizmente você assaltou alguém que não tinha nada em mãos...", color=0xef0027))
            
        money_hand = self.user.get_money_hand(ctx.guild.id, member.id)
        self.user.post_money_hand(ctx.guild.id, member.id, -money_hand)
        self.user.post_money_hand(ctx.guild.id, ctx.author.id, money_hand)

        frases = [f"Vish, me parece que o {member.mention} acabou de ser roubado...", f"Um vagabundo acabou de roubar o {member.mention}.",
                f"Infelizmente o {member.mention} acabou de ser roubado...", f"Uma camera flagrou o vagabundo do {ctx.author.mention}, roubando o {member.mention}.",
                f"Hmm... o {ctx.author.mention} foi pego no flagra roubando o {member.mention}"]

        x = randrange(len(frases))
        await ctx.send(embed=discord.Embed(description=frases[x], color=0x6600db))

    @commands.command(name="caça-niquel", aliases=["casanik", "jogo-do-bicho"])
    async def _caça(self, ctx):
        if self.guild.get_system_economy(ctx.guild.id) == 'False':
            return await ctx.send(embed=discord.Embed(description=f"{BankI} Sistema de economia está desativado neste grupo.", color=0xef0027).set_footer(text="Para tivar use o comando: [p]set economy"))

        hand = self.user.get_money_hand(ctx.guild.id, ctx.author.id)
        casanikMoney = self.bot.get_casanik(ctx.guild.id, self.client.user.id)
        if hand >= 100:
            self.user.post_money_hand(ctx.guild.id, ctx.author.id, -100)
            self.bot.post_casanik(ctx.guild.id, self.client.user.id, 100)

            a = randrange(len(self.casanik_icons))
            b = randrange(len(self.casanik_icons))
            c = randrange(len(self.casanik_icons))
            d = randrange(len(self.casanik_icons))
            e = randrange(len(self.casanik_icons))

            slotmachine = f"└──[ {self.casanik_icons[a]} {self.casanik_icons[b]} {self.casanik_icons[c]} {self.casanik_icons[d]} {self.casanik_icons[e]} ]──┘ \n{ctx.author.mention}"
            if a == b == c == d == e:
                self.bot.post_casanik(ctx.guild.id, self.client.user.id, 0)
                self.user.post_money_hand(ctx.guild.id, ctx.author.id, casanikMoney)
                await ctx.send(embed=discord.Embed(title=f"{CasanikI} - Games", color=0x00ef5b, description=f"{slotmachine}, {WinI} **BINGO!!!!** Prêmio: **${casanikMoney}** {ConfettiI}").set_footer(text="Seu prêmio está em suas mãos cuidado para não ser roubado!"))
            else:
                await ctx.send(embed=discord.Embed(title=f"{CasanikI} - Games", color=0xef0027, description=f"{slotmachine} Desculpe não foi desta vez, tente novamente... 😢").set_footer(text=f"Prêmio acumulado: ${casanikMoney}"))
        else:
            await ctx.send(embed=discord.Embed(title=f"{CasanikI} - Games", color=0xef0027, description="Você não possui dinheiro suficiente em suas mãos para jogar."))

    @commands.command(name="sorteio")
    async def sortition(self, ctx, x1:int=0, x2:int=50):
        x = randint(x1, x2)
        await ctx.send(embed=discord.Embed(description=f"<:clover:572462775402496031> Numero ganhador é {x} {ConfettiI}", color=0x00ef5b))

    @commands.command(aliases=['anom', 'diz'])
    async def anonimo(self, ctx, *, msg: str):
        await ctx.message.delete()
        await ctx.send(msg)

def setup(client):
    client.add_cog(MyFunny(client))