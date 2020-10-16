from PIL import Image, ImageDraw, ImageFont, ImageOps
from Commands.Utils.icons import getIcon
from discord.ext import commands, tasks
from newsapi import NewsApiClient
from datetime import datetime
from os import system, getpid
from bs4 import BeautifulSoup
from itertools import cycle
from asyncio import sleep
from io import BytesIO
from json import load
from discord.ext import menus
from Database import *

import discord, requests
import time, psutil

"""
    A classe "database" está sendo importada pelo "from Database import *", ela está dentro do __init__.py dentro da pasta "Database".
"""

i_covid         = getIcon("Covid 19")
i_ativos        = getIcon("Covid Cases Actives")
i_recuperados   = getIcon("Covid Cases Recovered")
i_mortos        = getIcon("Covid Cases Fatal")
i_news          = getIcon("Covid News")
i_module        = getIcon("Module")
i_moduleError   = getIcon("Module Error")
i_moduleWarning = getIcon("Module Warning")

MongoDBI   = "<:mongodb:571423025216487435>"
MsgEditI   = "<:messageedit:572170279934230560>"
MsgDelI    = "<:messagedel:572135356619554837>"
MsgI       = "<:message:571547016367308813>"
MsgEdit2I  = "<:messageedit:572136907417321482>"
BanI       = "<:ban:572158089533587457>"
UnbanI     = "<:unban:572158089630056458>"
KickI      = "<:kick:572158089155837999>"
AdminI     = "<:admin:473318484852604929>"
ReasonI    = "<:reason:572159935312298024>"
ArrowRI    = "<:arrowright:572241056087932931>"
ArrowDI    = "<:arrowdown:572241055982944259>"
EditImgI   = "<:editimg:572249725131292672>"
EditNameI  = "<:editname:572249725189881886>"
IdI        = "<:id:473326370622013450>"
NameI      = "<:name:473334939991932928>"
NameUpI    = "<:nameup:572254330992721950>"
NameDownI  = "<:namedown:572254330715897877>"
VoiceI     = "<:voice:473316669041803264>"
VoiceUpI   = "<:voiceup:574710363560476709>"
VoiceDownI = "<:voicedown:574710364000878607>"

if SHARD:
    client = commands.AutoShardedBot(shard_count=10, shard_id=(1,2,3,4,5,6), command_prefix=PREFIX_DEFAULT, owner_id=OWNERID, case_insensitive=True)
else:
    client = commands.Bot(command_prefix=commands.when_mentioned_or(PREFIX_DEFAULT), owner_id=OWNERID, case_insensitive=True)

class Uptime:
    def __init__(self):
        self.MINUTE = 60
        self.HOUR = self.MINUTE * 60
        self.DAY = self.HOUR * 24
        self.startTime = time.time()

    def total(self):
        total_seconds = float(time.time() - self.startTime)
        string = ""

        days = int(total_seconds / self.DAY)
        hours = int((total_seconds % self.DAY) / self.HOUR)
        minutes = int((total_seconds % self.HOUR) / self.MINUTE)
        seconds = int(total_seconds % self.MINUTE)

        if days > 0:
            string += f"{days} {(days == 1 and 'dia' or 'dias')}, "
        if len(string) > 0 or hours > 0:
            string += f"{hours} {(hours == 1 and 'hora' or 'horas')}, "
        if len(string) > 0 or minutes > 0:
            string += f"{minutes} {(minutes == 1 and 'minuto' or 'minutos')}, "

        string += f"{seconds} {(seconds == 1 and 'segundo' or 'segundos')} "

        return string

    def numbers(self):
        total_seconds = float(time.time() - self.startTime)
        string = ""

        days = int(total_seconds / self.DAY)
        hours = int((total_seconds % self.DAY) / self.HOUR)
        minutes = int((total_seconds % self.HOUR) / self.MINUTE)
        seconds = int(total_seconds % self.MINUTE)

        if days > 0:
            string += f"{days}:"
        if len(string) > 0 or hours > 0:
            string += f"{hours}:"
        if len(string) > 0 or minutes > 0:
            string += f"{minutes}:"

        string += f"{seconds}"

        return string

@tasks.loop(seconds=10)
async def loop_status():
    await client.change_presence(activity=discord.Game(next(client.status)))

@loop_status.before_loop
async def wait_for_bot():
    await client.wait_until_ready()
    client.status = cycle([f"Ping: {int(client.latency*1000)}ms", "Digite: .help", f"Ram: {psutil.Process(getpid()).memory_info().rss / 4194304:.2f} MB"])

class MyClient(commands.Cog, name="Client"):
    def __init__(self, client):
        self.client   = client
        self.check    = database.check()
        self.guild    = database.guild()
        self.user     = database.user()
        self.bot      = database.bot()
        self.uptime   = Uptime()
        self.json  = {
             "E0":"<:zero:571424008084389905>",
             "E1":"<:one:571424007967080449>",
             "E2":"<:two:571424008189378577>",
             "E3":"<:three:571424007723679783>",
             "E4":"<:four:571424008315207690>",
             "E5":"<:five:571424008147566622>",
             "E6":"<:six:571424007887519748>",
             "E7":"<:seven:571424007971405876>",
             "E8":"<:eight:571424008072069142>",
             "E9":"<:nine:571424008130527272>"}

    async def modules_start(self, modules=MODULES):
        for x in modules:
            try:
                self.client.load_extension("Commands."+x)
                print("[+] Modulo %s carregado com sucesso!" % x)
            except Exception as e:
                print("[!] Modulo %s com erro no carregamento!" % x)
                if input("[?] Deseja ver o erro ? [Sim/Não]$ ").lower() in ["yes","y", "sim","s"]:
                    print("[!] Erro: %s" % e)
                    pass
                else:
                    pass

    async def on_ready(self):
        print("Logado no bot: %s(%s) \nServidores: %s \nUsuários: %s" % (self.client.user, self.client.user.id, 1, 1))

        def check_is_bot(member):
            if not member.id == self.client.user.id and member.bot is False:
                return True

        for guild in self.client.guilds:
            if self.check.guild(guild.id) is False:
                self.guild.create(guild.id, guild.owner.id)
                print("[?] Servidor: %s(%s) de %s(%s), foi configurado na database! [Inicialização]" % (member.name, member.id, guild.owner.name, guild.owner.id))

            if self.check.bot(guild.id, self.client.user.id) is False:
                self.bot.create(guild.id, self.client.user.id)

            for member in guild.members:
                if check_is_bot(member):
                    if self.check.user(guild.id, member.id) is False:
                        self.user.create(guild.id, member.id)
                        print("[?] Usuário: %s(%s) do servidor %s(%s) foi configurado na database! [Inicialização]" % (member.name, member.id, guild.name, guild.id))

        await self.modules_start()

    async def on_message(self, ctx):
        if self.check.guild(ctx.guild.id) and not ctx.author.id == self.client.user.id and ctx.author.bot == False:
            
            if self.guild.get_auto_react(ctx.guild.id) == ctx.channel.id: # Sistema de auto react
                await ctx.add_reaction('👍')
                await ctx.add_reaction('👎')

            if self.check.user(ctx.guild.id, ctx.author.id) == True:
                if not self.guild.get_system_xp_level(ctx.guild.id) == "False": # Sistema de LEVEL & XP
                    self.user.post_xp(ctx.guild.id, ctx.author.id)
                    self.user.post_level(ctx.guild.id, ctx.author.id)

                self.user.post_messages(ctx.guild.id, ctx.author.id) # Sistema de contagem de mensagens

    async def on_guild_join(self, guild):
        if self.check.guild(guild.id) is False:
            self.guild.create(guild.id, guild.owner.id)
            self.bot.create(guild.id, self.client.user.id)

    async def on_guild_remove(self, guild):
        if self.check.guild(guild.id) is True:
            self.guild.delete(guild.id)
            self.bot.delete(guild.id)

    async def on_member_join(self, member):
        if self.check.user(member.guild.id, member.id):
            self.user.create(member.guild.id, member.id)

        if self.check.guild(member.guild.id):
            auto_role = self.guild.get_auto_role(member.guild.id)
            counter  = self.guild.get_counter(member.guild.id)
            welcome  = self.guild.get_welcome(member.guild.id)

            if welcome != 0:
                Font   = ImageFont.truetype('Utils/Fonts/Roboto-Thin.ttf', 25)
                Ball   = Image.open("Utils/Icons/ball.png").resize((60, 59))
                Fundo  = Image.open("Utils/Images/welcome.png")

                Status = Image.open('Utils/Icons/offline.png').resize((55, 55))
                if member.status == "online":
                    Status = Image.open('Utils/Icons/online.png').resize((55, 55))
                if member.status == "offline":
                    Status = Image.open('Utils/Icons/offline.png').resize((55, 55))
                if member.status == "dnd":
                    Status = Image.open('Utils/Icons/dnd.png').resize((55, 55))
                if member.status == "idle":
                    Status = Image.open('Utils/Icons/idle.png').resize((55, 55))

                Avatar = Image.open(BytesIO(requests.get(member.avatar_url).content))
                Avatar = Avatar.resize((153, 153))
                BigSize = (Avatar.size[0] * 3, Avatar.size[1] * 3)
                Mask = Image.new('L', BigSize, 0)
                Draw = ImageDraw.Draw(Mask)
                Draw.ellipse((0, 0) + BigSize, fill=255)
                Mask = Mask.resize(Avatar.size, Image.ANTIALIAS)

                Avatar.putalpha(Mask)
                Output = ImageOps.fit(Avatar, Mask.size, centering=(0.5, 0.5))
                Output.putalpha(Mask)
                Output.save("Utils/Images/avatar.png")

                Background = Image.open(BytesIO(requests.get("https://i.imgur.com/9Pac4rw.png").content))
                Write = ImageDraw.Draw(Fundo)
                Write.text(xy=(217, 15), text=f"Seja bem-vindo(a).", fill=(255, 255, 255), font=Font)
                Write.text(xy=(205, 165), text=member.name, fill=(255, 255, 255), font=Font)

                Background.paste(Fundo, (0, 0), Fundo)
                Background.paste(Avatar, (32, 75), Avatar)
                Background.paste(Ball, (150, 152), Ball)
                Background.paste(Status, (152, 154), Status)
                Background.save('Utils/Images/welcomeF.png')

                await self.client.get_channel(welcome).send(f"{member.mention} Seja bem-vindo(a) ao grupo {member.guild.name}.", file=discord.File("Utils/Images/welcomeF.png", filename=f"Welcome-de-{member.name}.png"))
                system('rm Utils/Images/welcomeF.png && rm Utils/Images/avatar.png')

            if auto_role != 0:
                await member.add_roles(discord.utils.get(member.guild.roles, id=auto_role))

            if counter != 0:
                text = str(len(member.guild.members))
                for n in range(0, 10):
                    text = text.replace(str(n), f"E{n}")
                for n in range(0, 10):
                    text = text.replace(f"E{n}", self.json[f"E{n}"])

                await self.client.get_channel(counter).edit(topic=f'Membros: {text} <:up:571433457117560833>')

    async def on_member_remove(self, member):
        if self.check.user(member.guild.id, member.id):
            self.user.delete(member.guild.id, member.id)

        if self.check.guild(member.guild.id):
            logs    = self.guild.get_logs(member.guild.id)
            counter = self.guild.get_counter(member.guild.id)

            if counter != 0:
                text = str(len(member.guild.members))
                for n in range(0, 10):
                    text = text.replace(str(n), f"E{n}")
                for n in range(0, 10):
                    text = text.replace(f"E{n}", self.json[f"E{n}"])

                await self.client.get_channel(counter).edit(topic=f'Membros: {text} <:down:571433457457299478>')

            if logs != 0:
                async for entry in member.guild.audit_logs(action=discord.AuditLogAction.kick):
                    if entry.target.id == member.id:
                        embed = discord.Embed(title=f"{KickI} Logs - {member.name}", color=0xef0027, timestamp=datetime.utcnow())
                        embed.add_field(name=f"{NameI}Membro:", value=f"```{entry.target}```")
                        embed.add_field(name=f"{AdminI}Admin:", value=f"```{entry.user}```")
                        embed.add_field(name=f"{ReasonI}Motivo:", value=f"```{entry.reason}```", inline=False)
                        return await self.client.get_channel(logs).send(embed=embed)

    async def on_member_update(self, before, after):
        if self.check.guild(after.guild.id):
            Logs = self.guild.get_logs(after.guild.id)
            if Logs != 0:
                if after.nick != before.nick:
                    embed = discord.Embed(title=f"{EditNameI} Logs - {after.guild.name}", color=0x00a3ef, timestamp=datetime.utcnow())
                    embed.add_field(name=f"{IdI}ID:", value=f"```{after.id}```", inline=False)
                    embed.add_field(name=f"{NameDownI}Antigo:", value=f"```{str(before.nick).replace('None', before.name)}```", inline=False)
                    embed.add_field(name=f"{NameUpI}Novo:", value=f"```{str(after.nick).replace('None', after.name)}```", inline=False)
                    return await self.client.get_channel(Logs).send(embed=embed)

                if after.avatar != before.avatar:
                    embed = discord.Embed(title=f"{EditImgI} Logs - {after.guild.name}", color=0x00a3ef, timestamp=datetime.utcnow())
                    embed.add_field(name=f"{NameI}Nome:", value=f"```{after.name}```\n{ArrowRI}Antigo\n{ArrowDI}Novo")
                    embed.set_image(url=f"https://cdn.discordapp.com/avatars/{after.id}/{after.avatar}.webp?size=1024")
                    embed.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{before.id}/{before.avatar}.webp?size=1024")
                    return await self.client.get_channel(Logs).send(embed=embed)

    async def on_member_ban(self, guild, user):
        if self.check.user(guild.id, user.id):
            self.user.delete(guild.id, user.id)

        if self.check.guild(guild.id):
            logs = self.guild.get_logs(guild.id)
            if logs != 0:
                async for entry in guild.audit_logs(action=discord.AuditLogAction.ban):
                    if entry.target.id == user.id:
                        embed = discord.Embed(title=f"{BanI} Logs - {guild.name}", color=0xef0027, timestamp=datetime.utcnow())
                        embed.add_field(name=f"{NameI}Membro:", value=f"```{entry.target}```")
                        embed.add_field(name=f"{AdminI}Admin:", value=f"```{entry.user}```")
                        embed.add_field(name=f"{ReasonI}Motivo:", value=f"```{entry.reason}```", inline=False)
                        return await self.client.get_channel(logs).send(embed=embed)

    async def on_member_unban(self, guild, user):
        if self.check.guild(guild.id):
            logs = self.guild.get_logs(guild.id)
            if logs != 0:
                async for entry in guild.audit_logs(action=discord.AuditLogAction.unban):
                    if entry.target.id == user.id:
                        embed = discord.Embed(title=f"{UnbanI} Logs - {guild.name}", color=0xef0027, timestamp=datetime.utcnow())
                        embed.add_field(name=f"{NameI}Usuário:", value=f"```{entry.target}```")
                        embed.add_field(name=f"{AdminI}Admin:", value=f"```{entry.user}```", inline=False)
                        return await self.client.get_channel(logs).send(embed=embed)

    async def on_message_edit(self, before, after):
        if after.author.bot:
            return

        if self.check.guild(after.guild.id):
            logs = self.guild.get_logs(after.guild.id)
            if logs != 0:
                embed = discord.Embed(description=f"[{MsgEditI} Logs - {after.channel.name}](https://discordapp.com/channels/{after.guild.id}/{after.channel.id}/{after.id})", color=0x444444, timestamp=datetime.utcnow())
                embed.add_field(name=f"{NameI}Nome:", value=f"```{after.author.name}```")
                embed.add_field(name=f"{IdI}ID:", value=f"```{after.author.id}```")
                embed.add_field(name=f"{MsgI}Mensagem Original:", value=f"```{after.content}```", inline=False)
                embed.add_field(name=f"{MsgEdit2I}Mensagem Editada:", value=f"```{before.content}```", inline=False)
                return await self.client.get_channel(logs).send(embed=embed)

    async def on_message_delete(self, message):
        async for entry in message.guild.audit_logs(action=discord.AuditLogAction.unban):
            if message.author.id == entry.target.id:
                return

        if message.author.bot:
            return

        if self.check.guild(message.guild.id):
            Logs = self.guild.get_logs(message.guild.id)
            if Logs != 0:
                embed = discord.Embed(title=f"{MsgDelI} Logs - {message.channel.name}", color=0x444444, timestamp=datetime.utcnow())
                embed.add_field(name=f"{NameI}Nome:", value=f"```{message.author.name}```")
                embed.add_field(name=f"{IdI}ID:", value=f"```{message.author.id}```")
                embed.add_field(name=f"{MsgI}Mensagem Apagada:", value=f"```{message.content}```", inline=False)
                return await self.client.get_channel(Logs).send(embed=embed)

    async def on_voice_state_update(self, member, before, after):
        if self.check.guild(member.guild.id):
            Logs = self.guild.get_logs(member.guild.id)
            if Logs != 0:
                if not after.channel is None:
                    embed = discord.Embed(title=f"{VoiceUpI} Logs - {member.guild.name}", color=16761645, timestamp=datetime.utcnow())
                    embed.add_field(name=f"{NameI}Nome:", value=f"```{member.name}```")
                    embed.add_field(name=f"{IdI}ID:", value=f"```{member.id}```")
                    embed.add_field(name=f"{VoiceI}Canal:", value=f"```{after.channel.name}```", inline=False)
                    await self.client.get_channel(Logs).send(embed=embed)
                else:
                    embed = discord.Embed(title=f"{VoiceDownI} Logs - {member.guild.name}", color=16761645, timestamp=datetime.utcnow())
                    embed.add_field(name=f"{NameI}Nome:", value=f"```{member.name}```")
                    embed.add_field(name=f"{IdI}ID:", value=f"```{member.id}```")
                    embed.add_field(name=f"{VoiceI}Canal:", value=f"```{before.channel.name}```", inline=False)
                    await self.client.get_channel(Logs).send(embed=embed)

class MyCommand(commands.Cog, name="Command"):
    def __init__(self, client):
        self.client = client
        self.uptime = Uptime

    @client.check
    async def globally_check_command(ctx):
        check  = database.check()
        guild  = database.guild()
        user   = database.user()
        bot    = database.bot()

        if check.guild(ctx.guild.id) == False:
            guild.create(ctx.guild.id, ctx.guild.owner.id)
            await ctx.send(embed=discord.Embed(description=f"{ctx.guild.owner}, Por favor! Execute o comando novamente. Ocorreu um erro! Seu servidor não estava configurado na minha database. Mas agora está!", color=0xef0027))
            return False

        if check.user(ctx.guild.id, ctx.author.id) == False:
            user.create(ctx.guild.id, ctx.author.id)
            await ctx.send(embed=discord.Embed(description=f"{ctx.author.id}, Por favor! Execute o comando novamente. Ocorreu um erro! Aparentemente você não estava configurado na minha database. Mas agora está!", color=0xef0027))
            return False

        if check.bot(ctx.guild.id, BOTID) == False:
            bot.create(ctx.guild.id, BOTID)
            await ctx.send(embed=discord.Embed(description=f"{ctx.guild.owner}, Por favor! Execute o comando novamente. Ocorreu um erro!", color=0xef0027))
            return False

        if not guild.get_whitelist(ctx.guild.id) == ctx.channel.id and not guild.get_whitelist(ctx.guild.id) == 0 and not ctx.author.id == ctx.guild.owner.id:
            await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention}, você não pode executar comandos nesse chat.", color=0xef0027))
            return False

        return True

    @commands.command(name="load")
    @commands.is_owner()
    async def _load(self, ctx, extension_name: str):
        try:
            self.client.load_extension(f"Commands.{extension_name}")
            await ctx.send(embed=discord.Embed(description=f"{i_module} O modulo `{extension_name}` foi carregado com sucesso!", color=0x444444))
        except Exception as e:
            await ctx.send(embed=discord.Embed(description=f"{i_moduleError} Ocorreu um erro ao carregar o modulo: `{type(e).__name__}` - `{e}`", color=0xef0027))

    @commands.command(name="unload")
    @commands.is_owner()
    async def _unload(self, ctx, extension_name: str):
        try:
            self.client.unload_extension(f"Commands.{extension_name}")
            await ctx.send(embed=discord.Embed(description=f"{i_module} Modulo `{extension_name}` foi descarregado", color=0x444444))
        except Exception as e:
            await ctx.send(embed=discord.Embed(description=f"{i_moduleError} ERROR: {type(e).__name__} - {e}", color=0xef0027))

    @commands.command(name="reload")
    @commands.is_owner()
    async def _reload(self, ctx, extension_name: str):
        try:
            self.client.unload_extension(f"Commands.{extension_name}")
            self.client.load_extension(f"Commands.{extension_name}")
            await ctx.send(embed=discord.Embed(description=f"{i_module} Modulo `{extension_name}` esta sendo recarregado", color=0x444444))
        except Exception as e:
            await ctx.send(embed=discord.Embed(description=f"{i_moduleError} ERROR: {type(e).__name__} - {e}", color=0xef0027))

client.add_cog(MyClient(client))
client.add_cog(MyCommand(client))

client.add_listener(MyClient(client).on_ready)
client.add_listener(MyClient(client).on_message)

client.add_listener(MyClient(client).on_member_join)
client.add_listener(MyClient(client).on_member_remove)
client.add_listener(MyClient(client).on_guild_join)
client.add_listener(MyClient(client).on_guild_remove)

client.add_listener(MyClient(client).on_member_ban)
client.add_listener(MyClient(client).on_member_unban)
client.add_listener(MyClient(client).on_member_update)

client.add_listener(MyClient(client).on_message_delete)
client.add_listener(MyClient(client).on_message_edit)

client.add_listener(MyClient(client).on_voice_state_update)

loop_status.start()
client.run(TOKEN, bot=True)