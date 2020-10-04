from discord.ext import commands
from datetime import datetime
from Database import *

import discord, asyncio
import inspect, typing
import re

IdI         = "<:id:473326370622013450>"
WelI        = "<:welcome:572480320344162325>"
HddI        = "<:hdd:571174665121169418>"
MuteI       = "<:mute:574781872828317696>"
NameI       = "<:name:473334939991932928>"
HintI       = "<:hint:571396019322093580>"
LogsI       = "<:logs:572463446487072778>"
TimeI       = "<:tempo:473320586538385420>"
AdminI      = "<:admin:473318484852604929>"
UnMuteI     = "<:unmute:574781872589242399>"
MongoDBI    = "<:mongodb:571423025216487435>"
CounterI    = "<:counter:572481181086646292>"
ScienceI    = "<:sciencefiction:572482102633824265>"
SilenceI    = "<:silence:572483419389427723>"
TrashI      = "<:trash:577292624810213406>"
RunCommandI = "<:runcommand:616018223913238538>"

time_regex = re.compile("(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {"h":3600, "s":1, "m":60, "d":86400}

class TimeConverter(commands.Converter, commands.Cog):
    async def convert(self):
        args = self.argument.lower()
        matches = re.findall(time_regex, args)
        time = 0
        for v, k in matches:
            try:
                time += time_dict[k]*float(v)
            except KeyError:
                raise commands.BadArgument(f"{k} é uma chave de tempo inválida! h/m/s/d é válido!!")
            except ValueError:
                raise commands.BadArgument(f"{v} não é um número!")
        return time

class MemberID(commands.Converter, commands.Cog):
    async def convert(self, ctx, argument):
        try:
            m = await commands.MemberConverter().convert(ctx, argument)
        except commands.BadArgument:
            try:
                return int(argument, base=10)
            except ValueError:
                raise commands.BadArgument(f"{argument} não é um membro ou ID de membro válido.") from None
        else:
            can_execute = ctx.author.id == ctx.bot.owner_id or \
                          ctx.author == ctx.guild.owner or \
                          ctx.author.top_role > m.top_role

            if not can_execute:
                raise commands.BadArgument('Você não pode fazer essa ação nesse usuário devido à hierarquia de cargos.')
            return m.id

class MyOwner(commands.Cog, name="Administração"):
    def __init(self, client):
        self.client   = client
        self.guild = database.guild()
        self.check = database.check()

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(manage_roles=True)
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member:discord.Member=None, *, time:TimeConverter=None):
        MuteRole = self.guild.get_mute_role(ctx.guild.id)
        Logs     = self.guild.get_logs(ctx.guild.id)

        if MuteRole == 0:
            return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention}, este comando está desativado neste servidor.", color=0xef0027))
        if member is None:
            return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention}, é necessário você está informando o usuário.", color=0xef0027))
        if time is None:
            return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention}, você não informou o tempo de mute.", color=0xef0027))

        role = discord.utils.get(ctx.guild.roles, id=MuteRole)
        await member.add_roles(role)

        if Logs != 0:
            embed = discord.Embed(title=f"{MuteI} Logs - {ctx.guild.name}", color=0xef0027, timestamp=datetime.utcnow())
            embed.add_field(name=f"{NameI}Nome:", value=f"```{member.name}```", inline=False)
            embed.add_field(name=f"{IdI}ID:", value=f"```{member.id}```", inline=True)
            embed.add_field(name=f"{AdminI}Admin:", value=f"```{ctx.author.name}```", inline=False)
            embed.add_field(name=f"{IdI}ID:", value=f"```{ctx.author.id}```", inline=True)
            embed.add_field(name=f"{TimeI}Tempo:", value=f"```{time}```", inline=False)
            await self.client.get_channel(Logs).send(embed=embed)

        if not time is None:
            await asyncio.sleep(time)
            await member.remove_roles(role)
            if Logs != 0:
                embed = discord.Embed(title=f"{UnMuteI} Logs - {ctx.guild.name}", color=0xef0027, timestamp=datetime.utcnow())
                embed.add_field(name=f"{NameI}Nome:", value=f"```{member.name}```", inline=False)
                embed.add_field(name=f"{IdI}ID:", value=f"```{member.id}```", inline=True)
                embed.add_field(name=f"{AdminI}Admin:", value=f"```{ctx.author.name}```", inline=False)
                embed.add_field(name=f"{IdI}ID:", value=f"```{ctx.author.id}```", inline=True)
                embed.add_field(name=f"{TimeI}Tempo:", value=f"```{time}```", inline=False)
                await self.client.get_channel(Logs).send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(ban_members=True)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, members: commands.Greedy[discord.Member]=None, delete_days: typing.Optional[int]=0, *, reason:str="Motivo não informado!!"):
        if members is None:
            await ctx.send(embed=discord.Embed(description="Você não informou o usuário."))

        for member in members:
            await member.ban(delete_message_days=delete_days, reason=reason)

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(ban_members=True)
    @commands.has_permissions(ban_members=True)
    async def massban(self, ctx, reason:str=None, *members:MemberID):
        if reason is None:
            reason = "Não informado!!"

        for member_id in members:
            await ctx.guild.ban(member_id, reason=reason, delete_message_days=1)

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(kick_members=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member:discord.Member=None, *, reason:str=None):
        if member is None:
            return await ctx.send(embed=discord.Embed(description="Você não informou o membro.", color=0xef0027))
        if reason is None:
            reason = "Não informado!!"

        await member.kick(reason=reason)

    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(kick_members=True)
    @commands.has_permissions(kick_members=True)
    async def softban(self, ctx, member: discord.Member=None, *, reason:str="Não informado!!"):
        if member is None:
            return await ctx.send(embed=discord.Embed(description="Você não informou o membro.", color=0xef0027))

        await member.ban(reason=reason, delete_message_days=1)
        await ctx.guild.unban(member, reason=reason)

    @commands.command(aliases=['clean'], no_pm=True)
    @commands.guild_only()
    @commands.bot_has_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    async def limpar(self, ctx, number:int=50):
        if number > 100:
            return await ctx.send(embed=discord.Embed(description=f"Limite de 100 mensagens por vez. [**{number}/100**]", color=0xef0027))
        
        await ctx.channel.purge(limit=number)
        await ctx.send(embed=discord.Embed(description=f"{TrashI} **{number}** Mensagens apagadas.", color=0x5C6BC0), delete_after=30)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def eval(self, ctx, *, code: str=None):
        if code is None:
            return await ctx.send('Cade ?')

        code = code.strip('` ')
        python = '```py\n{}\n```'
        result = None
        env = {
            'await':'',
            'ctx': ctx,
            'self':'self.client',
            'client':'self.client',
            'message': ctx.message,
            'guild': ctx.guild,
            'channel': ctx.channel,
            'author': ctx.author,
        }
        env.update(globals())
        try:
            result = eval(code, env)
            if inspect.isawaitable(result):
                result = await result
        except Exception as e:
            return await ctx.send(embed=discord.Embed(color=0xef0027, title=f"{RunCommandI} Run Command - JrBlack", description=python.format((type(e).__name__ + ': ') + str(e))))
        
        embed = discord.Embed(title=f"{RunCommandI} Run Command - JrBlack", color=0x00ef5b)
        embed.add_field(name="📥Entrada:", value=f"```{code}```", inline=True)
        embed.add_field(name="📤Saída:", value=f"```{result}```", inline=True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(MyOwner(bot))
