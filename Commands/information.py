from PIL import Image, ImageDraw, ImageFont, ImageOps
from datetime import datetime, timedelta
from platform import python_version
from discord.ext import commands
from os import getpid, system
from random import randint
from io import BytesIO

from Database import OMBDBAPI, NEWSAPI, OMBDBAPI, WEATHERAPI
from Database import database

from . import sub_commands
from Commands.Utils.icons import getIcon

import discord, psutil
import aiohttp, time
import glob
import wikipedia
import requests

NameI         = getIcon("Name")
IdI           = getIcon("ID")
AvatarI       = getIcon("Photo")
StatusI       = getIcon("Status")
ActivityI     = getIcon("Activity")
DiscordI      = getIcon("Discord")
CalendarI     = getIcon("Calendar")
PngI          = getIcon("Png")
GifI          = getIcon("Gif")
ChatI         = getIcon("Chat")
VoiceI        = getIcon("Chat Voice")
MessageI      = getIcon("Chat Message")
CloseI        = getIcon("Padlock locked")
OpenI         = getIcon("Padlock unlocked")
LocationI     = getIcon("Location")
ColorI        = getIcon("Color Picker")
AboutI        = getIcon("About")
HddI          = getIcon("HD")
BankI         = getIcon("Bank")
CounterI      = getIcon("Counter")
UrlI          = getIcon("Website")
LinkI         = getIcon("Website")
InventoryI    = getIcon("Inventory")
PicapauI      = getIcon("Pica Pau")
OwnerI        = getIcon("Owner")
ResumeI       = getIcon("Profile Resume")
MembersI      = getIcon("Members")
BotI          = "<:bottag:473320587083907072>"
OnI           = "<:online:478924922228310049>"
OffI          = "<:offline:478924922199212042>"
DndI          = "<:ocupado:478924922228310027>"
AfkI          = "<:ausente:478924921943359499>"
WelI          = "<:welcome:572480320344162325>"
HintI         = "<:hint:571396019322093580>"
LogsI         = "<:logs:572463446487072778>"
MongoDBI      = "<:mongodb:571423025216487435>"
ScienceI      = "<:sciencefiction:572482102633824265>"
SilenceI      = "<:silence:572483419389427723>"
SettingsI     = "<:settings:473325105787699211>"
SpotifyI      = "<:spotify:579033031789248512>"
SpotifyErrorI = "<:spotifyError:579033029536776203>"
TimerI        = "<:timer:579033029616599040>"
MicrofoneI    = "<:microfone:579045198282227712>"
TagI          = "<:tag:579056961438482443>"
AlbumI        = "<:album:579045198286553088>"
XpI           = "<:xp:579101543760920597>"
LevelI        = "<:level:579101544226750474>"
PythonI       = "<:python:473316669071032330>"
PhpI          = "<:php:473337687341006919>"
DeveloperI    = "<:developer:473316669972807700>"
TimeI         = "<:tempo:473320586538385420>"
RamI          = "<:memory:473316669016506369>"
PingI         = "<a:ping:492865676998869023>"
ModulesI      = "<:modules:473334243028762624>"
CommandsI     = "<:command:488511365456068619>"
MortyI        = "<:morty:473337006248689664>"
CodeI         = "<:sourcecode:473326031529574432>"
HatdayI       = "<:4hatday:473336489053257729>"
GuildsI       = "<:guilds:473325247870009356>"
ReportCardI   = "<:reportcard:616313507964649503>"
DirectorI     = "<:director:616313506513420308>"
ImdbI         = "<:imdb:616313506144190493>"
ActorsI       = "<:actors:616313506500837378>"
ThrillerI     = "<:thriller:616028986648035359>"
AdventureI    = "<:adventures:616322075254325250>"
ScifiI        = "<:scifi:616322075904180461>"
SpyI          = "<:spy:616322075832877067>"
AgentI        = "<:agent:616322075270840351>"
DramaI        = "<:drama:616322075719893017>"
DocumentaryI  = "<:documentary:616322075522760740>"
MusicalI      = "<:musical:616322075682144267>"
ActionI       = "<:action:616322075895791685>"
AnimationI    = "<:animation:616322075636006938>"
RomanceI      = "<:romance:616322075904180247>"
HorrorI       = "<:horror:616322076214689803>"
WarI          = "<:tank:616329078332719115>"
ComedyI       = "<:comedy:616322075958706196>"
SpeedI        = "<:velocimetro:473610781246619700>"
CoordeI       = "<:globo:473318484630175756>"
MoistureI     = "<:umidade:473610781175316482>"
TempI         = "<:temperatura:473610781385162762>"
FogI          = "<:fog:483352973712424961>"
CloudyI       = "<:cloudy:483353555638419456>"
RainI         = "<:rain:483352982763864064>"
ClearI        = "<:clear:483353555714179082>"
DrizzleI      = "<:drizzler:483352982520594433>"
StormI        = "<:storm:483352982985900044>"
NewsI         = "<:news:473318485028634624>"
TitleI        = "<:tag:473316668848996353>"
DescI         = "<:instapper:473464976896557067>"
WriterI       = "<:write:473463839841845249>"
WikiI         = "<:wikipedia:493633468929146880>"
WeatherMapI   = "<:OpenWeatherMap:618913968936845323>"

start_time = time.time()

class MemoryRam:
    def __init__(self):
        self.mem     = psutil.virtual_memory()
        self.process = psutil.Process(getpid()).memory_info().rss

    def used(self):
        return f"{self.mem.used / 0x40_000_000:.2f} MB"

    def available(self):
        return f"{self.mem.available / 0x40_000_000:.2f} GB"

    def total(self):
        return f"{self.mem.total / 0x40_000_000:.2f} GB"

    def free(self):
        return f"{self.mem.free / 0x40_000_000:.2f} GB"

    def percent(self):
        return f"{self.mem.percent}%"

    def process_python(self):
        return f"{self.process / 4194304:.2f} MB"

class RequestApi:
    async def weather(self, location: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHERAPI}") as request:
                request = await request
        return request.json(), request.status()

    async def omdb(self, film: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://www.omdbapi.com/?apikey={OMBDBAPI}&t={film}") as request:
                request = await request
        return request.json(), request.status()

    async def news(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://newsapi.org/v2/top-headlines?sources=google-news-br&apiKey={NEWSAPI}") as request:
                request = await request
        return request.json(), request.status()

class MyInformation(commands.Cog, name="Informações"):
    def __init__(self, client):
        self.client = client
        self.ram    = MemoryRam()
        self.request= RequestApi()
        self.guild  = database.guild()
        self.user   = database.user()
        self.check  = database.check()

    @commands.group(name="info", aliases=["informação", "information"], usage="[p]info [sub comando]")
    @commands.guild_only()
    async def _info(self, ctx):
        if ctx.invoked_subcommand is None:
            return await sub_commands(self.client, ctx, ctx.command.name)

    @_info.command(aliases=["inven", "inventory"], usage="[p]info inventario")
    @commands.guild_only()
    async def inventario(self, ctx):
        background = self.user.get_inventory_background(ctx.guild.id, ctx.author.id)
        weapon     = self.user.get_inventory_weapon(ctx.guild.id, ctx.author.id)

        x = "".join(background)
        if len(background) > 1:
            x = " **|** ".join(background)
            
        y = "".join(weapon)
        if len(weapon) > 1:
            y = " **|** ".join(weapon)

        fmt = (f"**Papel de parede:** {x}\n\n**Armas:** {y}")

        await ctx.send(embed=discord.Embed(title=f"{InventoryI} Inventário", color=0x6600db, description=fmt))

    @_info.command(aliases=["av"], usage="[p]info avatar [membro]")
    @commands.guild_only()
    async def avatar(self, ctx, member:discord.Member=None):
        if member is None:
            member = ctx.author
        
        await ctx.send(embed=discord.Embed(description=f"Avatar de {member.mention}, [**clique aqui**]({member.avatar_url}) para abrir no navegador.").set_image(url=member.avatar_url))

    @_info.command(usage="[p]info spotify [membro]")
    @commands.guild_only()
    async def spotify(self, ctx, user:discord.Member=None):
        if user is None:
            user = ctx.author
        if not user.activity.name == "Spotify":
            return await ctx.send(embed=discord.Embed(description=f"{SpotifyErrorI} Não encontrei o Spotify RPC", color=0xef0027))

        embed = discord.Embed(title=f"{SpotifyI} Informações Spotify - {ctx.guild.name}", color=0x1DEB48, timestamp=datetime.utcnow())
        embed.add_field(name=f"{NameI}Nome:", value=f"```{user.name}```")
        embed.add_field(name=f"{IdI}ID:", value=f"```{user.id}```")
        embed.add_field(name=f"{TagI}Título:", value=f"```{user.activity.title}```")
        embed.add_field(name=f"{AlbumI}Álbum:",value=f"```{user.activity.album}```")
        embed.add_field(name=f"{MicrofoneI}Artista(s):", value=f"```{(', ').join(user.activity.artists)}```")
        embed.add_field(name=f"{TimerI}Duração:", value=f"```{str(user.activity.duration)[2:7]}```")
        embed.add_field(name=f"{UrlI}Url:", value=f"```https://open.spotify.com/track/{user.activity.track_id}```", inline=False)
        embed.set_footer(text=f"Pedido por: {ctx.author.name}")
        embed.set_thumbnail(url=user.activity.album_cover_url)

        await ctx.send(embed=embed)

    @_info.command(name="config", aliases=["settings"], usage="[p]info config")
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def settings(self, ctx):
        if not self.check.guild(ctx.guild.id):
            return await ctx.send(embed=discord.Embed(description=f"{MongoDBI} Servidor não configurado!", color=0xef0027))

        embed = discord.Embed(title=f"{SettingsI} Informações Configurações - {ctx.guild.name}", color=0x444444,  timestamp=datetime.utcnow())
        embed.add_field(name=f"{LogsI}Logs:",         value=f"```#{discord.utils.get(ctx.guild.channels, id=self.guild.get_logs(ctx.guild.id))}```")
        embed.add_field(name=f"{WelI}Welcome:",       value=f"```#{discord.utils.get(ctx.guild.channels, id=self.guild.get_welcome(ctx.guild.id))}```")
        embed.add_field(name=f"{CounterI}Counter:",   value=f"```#{discord.utils.get(ctx.guild.channels, id=self.guild.get_counter(ctx.guild.id))}```")
        embed.add_field(name=f"{HddI}Hard Disk:",     value=f"```#{discord.utils.get(ctx.guild.channels, id=self.guild.get_harddisk(ctx.guild.id))}```")
        embed.add_field(name=f"{HddI}Hard Disk 2:",     value=f"```#{discord.utils.get(ctx.guild.channels, id=self.guild.get_harddisk_2(ctx.guild.id))}```")
        embed.add_field(name=f"{HddI}Hard Disk 3:",     value=f"```#{discord.utils.get(ctx.guild.channels, id=self.guild.get_harddisk_3(ctx.guild.id))}```")
        embed.add_field(name=f"{HintI}Auto React:",   value=f"```#{discord.utils.get(ctx.guild.channels, id=self.guild.get_auto_react(ctx.guild.id))}```")
        embed.add_field(name=f"{ScienceI}Auto Role:", value=f"```{discord.utils.get(ctx.guild.roles, id=self.guild.get_auto_role(ctx.guild.id))}```")
        embed.add_field(name=f"{SilenceI}Mute Role:", value=f"```{discord.utils.get(ctx.guild.roles, id=self.guild.get_mute_role(ctx.guild.id))}```")

        await ctx.send(embed=embed)

    @_info.command()
    @commands.guild_only()
    async def stats(self, ctx):
        await ctx.send(f"""```asciidoc
[Guild Stats]
  Membros            :: {len(ctx.guild.members)}
  Cargos             :: {len(ctx.guild.roles)}
  Canais             :: {len(ctx.guild.text_channels) + len(ctx.guild.voice_channels)}

[Bot Stats]
  Tempo em atividade :: a
  Bot modúlos ext    :: 6
  Bot comandos       :: {len(ctx.bot.all_commands)}
  Bot latência       :: {self.client.latency * 1000:.2f} ms
  Bot versão         :: 4.0
  Discord versão     :: {discord.__version__}

  Versão do python   :: {python_version()}
  Memória usada      :: {self.ram.used()}
  Memória disponível :: {self.ram.available()}
  Total de memória   :: {self.ram.total()}
  Livre de memória   :: {self.ram.free()}
  Processo do Python :: {self.ram.process_python()}```""")

    @_info.command(name="perfil", aliases=["profile"])
    @commands.guild_only()
    async def profile(self, ctx):
        if self.guild.get_system_xp_level(ctx.guild.id) == "False":
            return await ctx.send(embed=discord.Embed(description=f"{XpI} Para que este comando funcione é necessario que o **Sistema de Xp/Level** esteja ativo.", color=0xef0027).set_footer(text="Para ativar user o comando: [p]set xplevel"))
        if self.guild.get_system_economy(ctx.guild.id) == "False":
            return await ctx.send(embed=discord.Embed(description=f"{BankI} Para este comando funcionar é necessario que o **Sistema de Economia** esteja ativo.", color=0xef0027).set_footer(text="Para ativar use o comando: [p]set economy"))
        if self.check.user(ctx.guild.id, ctx.author.id) == "False":
            return await ctx.send(embed=discord.Embed(description=f"{BankI} Para este comando funcionar é necessario que você esteja configurado na minha database.", color=0xef0027).set_footer(text=f"Para configurar use o comando: {self.client.user.mention} !!"))

        Profile = Image.open("Commands/Utils/Utils_pil_edit/Images/profile.png")
        Font  = ImageFont.truetype("Commands/Utils/Utils_pil_edit/Fonts/Roboto-Thin.ttf", 25)
        Font2 = ImageFont.truetype("Commands/Utils/Utils_pil_edit/Fonts/Roboto-Thin.ttf", 18)

        backgroundI = self.user.get_background(ctx.guild.id, ctx.author.id)
        if backgroundI == "False":
            backgroundI = "https://i.imgur.com/9Pac4rw.png"

        Background = Image.open(BytesIO(requests.get(backgroundI).content))
        Background.paste(Profile, (0, 0), Profile)
        Background.save("Commands/Utils/Utils_pil_edit/Images/profileF.png")

        ProfileF = Image.open("Commands/Utils/Utils_pil_edit/Images/profileF.png")

        Avatar = Image.open(BytesIO(requests.get(ctx.author.avatar_url).content))
        Avatar = Avatar.resize((151, 145))
        BigSize = (Avatar.size[0] * 3, Avatar.size[1] * 3)
        Mask = Image.new("L", BigSize, 0)
        Draw = ImageDraw.Draw(Mask)
        Draw.ellipse((0, 0) + BigSize, fill=255)
        Mask = Mask.resize(Avatar.size, Image.ANTIALIAS)
        Avatar.putalpha(Mask)

        Output = ImageOps.fit(Avatar, Mask.size, centering=(0.5, 0.5))
        Output.putalpha(Mask)
        Output.save("Commands/Utils/Utils_pil_edit/Images/avatar.png")

        MoneyBank = self.user.get_money_bank(ctx.guild.id, ctx.author.id)
        MoneyHand = self.user.get_money_hand(ctx.guild.id, ctx.author.id)
        About     = (self.user.get_about(ctx.guild.id, ctx.author.id)).capitalize()
        Level     = self.user.get_level(ctx.guild.id, ctx.author.id)
        Xp        = self.user.get_xp(ctx.guild.id, ctx.author.id)

        Write = ImageDraw.Draw(ProfileF)

        if len(ctx.author.name) > 12:
            Write.text(xy=(253, 13), text=f"{(ctx.author.name)[0:12]}...", fill=(255, 255, 255), font=Font2)
        else:
            Write.text(xy=(253, 13), text=f"{ctx.author.name}", fill=(255, 255, 255), font=Font2)

        Write.text(xy=(152, 148), text=f"${MoneyBank+MoneyHand}", fill=(255, 255, 255), font=Font)
        Write.text(xy=(55, 186), text=str(Xp), fill=(255, 255, 255), font=Font)
        Write.text(xy=(158, 225), text=str(Level), fill=(255, 255, 255), font=Font)
        Write.text(xy=(290, 151), text=f"{(About)[:30]}\n{(About)[30:60]}\n{(About)[60:90]}\n{(About)[90:120]}\n{(About)[120:150]}", fill=(255, 255, 255), font=Font2)

        Avatar = Avatar.crop((0, 0, 150, 115))
        ProfileF.paste(Avatar, (30, 18), Avatar)

        if str(ctx.author.status) == "online":
            Status = Image.open("Commands/Utils/Utils_pil_edit/Icons/online.png").resize((55, 55))
            ProfileF.paste(Status, (144, 98), Status)
        elif str(ctx.author.status) == "offline":
            Status = Image.open("Commands/Utils/Utils_pil_edit/Icons/invisible.png").resize((55, 55))
            ProfileF.paste(Status, (144, 98), Status)
        elif str(ctx.author.status) == "dnd":
            Status = Image.open("Commands/Utils/Utils_pil_edit/Icons/dnd.png").resize((55, 55))
            ProfileF.paste(Status, (144, 98), Status)
        elif str(ctx.author.status) == "idle":
            Status = Image.open("Commands/Utils/Utils_pil_edit/Icons/idle.png").resize((55, 55))
            ProfileF.paste(Status, (144, 98), Status)

        ProfileF.save("Commands/Utils/Utils_pil_edit/Images/profileF.png")

        await ctx.send(file=discord.File("Commands/Utils/Utils_pil_edit/Images/profileF.png", filename=f"Perfil-de-{ctx.author.name}.png")) #embed=discord.Embed(color=0x444444).set_image(url=f"attachment://Perfil-de-{ctx.author.name}.png"))
        system(f"rm Commands/Utils/Utils_pil_edit/Images/avatar.png && rm Commands/Utils/Utils_pil_edit/Images/profileF.png")

    @_info.command(aliases=["usuário", "usuario", "my"], usage="[p]info [usuário/user] [Membro: Mention/ID] or [None]")
    @commands.guild_only()
    async def user(self, ctx, member:discord.Member=None):
        if member is None:
            member = ctx.author

        try:
            activity = str(member.activity.name)
        except AttributeError:
            activity = str(member.activity).replace('None', 'Não encontrado!')

        embed = discord.Embed(title=f"{ResumeI} Informações Membro - {ctx.guild.name}", color=member.color)
        embed.add_field(name=f"{NameI}Nome:", value=f"```{member.name}```")
        embed.add_field(name=f"{IdI}ID:", value=f"```{member.id}```")
        embed.add_field(name=f"{StatusI}Status:", value=f"```{member.status}```") #.replace('idle', 'Ausente').replace('dnd', 'Ocupado').replace('online', 'Online').replace('offline', 'Offline')
        embed.add_field(name=f"{ActivityI}Atividade:", value=f"```{activity}```")
        embed.add_field(name=f"{CalendarI}Entrou em:", value=f"```{member.joined_at.strftime('%d/%b/%Y')}|{member.joined_at.strftime('%H:%M')}```")
        embed.add_field(name=f"{DiscordI}Desde:", value=f"```{member.created_at.strftime('%d/%b/%Y')}|{member.created_at.strftime('%H:%M')}```")
        embed.add_field(name=f"🌀Maior cargo:", value=f"```{member.top_role}```")
        embed.add_field(name=f"{ColorI}Cor:", value=f"```{member.color}```")

        if self.guild.get_system_xp_level(ctx.guild.id) == 'True':
            embed.add_field(name=f"{LevelI}Nivel:", value=f"```{self.user.get_level(ctx.guild.id, member.id)}```")
            embed.add_field(name=f"{XpI}Xp:", value=f"```{self.user.get_xp(ctx.guild.id, member.id)}```")

        embed.add_field(name=f"{AboutI}Sobre:", value=f"```{self.user.get_about(ctx.guild.id, member.id)}```", inline=False)
        embed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=embed)

    @_info.command(aliases=["servidor"], usage="[p]info [servidor/guild]")
    @commands.guild_only()
    async def guild(self, ctx):
        guild = ctx.guild
        emojis = [str(x) for x in guild.emojis]
        lista = " **|** ".join(emojis)

        a = len([jr.status for jr in guild.members if jr.status == discord.Status.online]) # Online
        b = len([jr.status for jr in guild.members if jr.status == discord.Status.idle])  # Ausente
        c = len([jr.status for jr in guild.members if jr.status == discord.Status.dnd])  # Ocupado
        d = len([jr.id for jr in guild.members if jr.bot])                              # Bots
        e = len(ctx.guild.text_channels)                                               # Texto
        f = len(ctx.guild.voice_channels)                                             # Voz
        h = len([jr.id for jr in guild.members if jr.status == jr.status == discord.Status.offline]) # off
        i = len([jr for jr in guild.emojis if jr.animated is True])                                 #Animados
        j = len([jr for jr in guild.emojis if jr.animated is False])                               #Normais

        online = f"{a}"
        ausente = f"{b}"
        ocupado = f"{c}"
        offline = f"{h}"

        data = guild.created_at.strftime("%d %b %Y")
        hora = guild.created_at.strftime("%H:%M")

        embed = discord.Embed(title=f"Informações Servidor- {guild.name}", color=0x444444)
        embed.add_field(name=f"{NameI}Nome:", value=f"``{guild.name}``", inline=True)
        embed.add_field(name=f"{IdI}ID:", value=f"``{guild.id}``", inline=True)
        embed.add_field(name=f"{OwnerI}Dono:", value=f"``{guild.owner}``", inline=True)
        embed.add_field(name=f"🌀Cargos:", value=f"``{len(guild.roles)}``", inline=True)
        embed.add_field(name=f"{MembersI}Membros[{len(guild.members)}]:", value=f"{OnI}``{online}`` {DndI}``{ocupado}`` {AfkI}``{ausente}`` \n{OffI}``{offline}`` {BotI}``{d}``", inline=True)
        embed.add_field(name=f"{ChatI}Canais[{e + f}]:", value=f"{MessageI}``{e}`` {VoiceI}``{f}``")
        embed.add_field(name=f"{CalendarI}Criado em:", value=f"``{data}`` ``{hora}``", inline=True)
        embed.add_field(name=f"{PicapauI}Emojis[{len(guild.emojis)}/100]:", value=f"{PngI}:`{j}` {GifI}:`{i}`", inline=True)

        if str(guild.verification_level) == "none":
            embed.add_field(name=f"{OpenI}Nivel de verificação:", value="`Sem verificação`", inline=True)
        else:
            embed.add_field(name=f"{CloseI}Nivel de verificação:", value=f"`{str(guild.verification_level).replace('low', 'Baixo').replace('high', 'Alto')}`", inline=True)

        embed.set_thumbnail(url=guild.icon_url)

        Region = str(ctx.guild.region)

        if Region == "Brazil":
            embed.add_field(name=f"{LocationI}Região do server:", value="🇧🇷 `Brasil`")

        elif Region == "Us-Central":
            embed.add_field(name=f"{LocationI}Região do Server:", value=f"🇺🇸 ``{Region}``")
        elif Region == "Us-West":
            embed.add_field(name=f"{LocationI}Região do Server:", value=f"🇺🇸 ``{Region}``")
        elif Region == "Us-East":
            embed.add_field(name=f"{LocationI}Região do Server:", value=f"🇺🇸 ``{Region}``")
        elif Region == "Us-South":
            embed.add_field(name=f"{LocationI}Região do Server:", value=f"🇺🇸 ``{Region}``")

        elif Region == "Eu-Central":
            embed.add_field(name=f"{LocationI}Região do server:", value=f"🇪🇺 ``{Region}``")
        elif Region == "Eu-Western":
            embed.add_field(name=f"{LocationI}Região do server:", value=f"🇪🇺 ``{Region}``")

        elif Region == "Japan":
            embed.add_field(name=f"{LocationI}Região do server:", value=f"🇯🇵 ``{Region}``")
        elif Region == "Russia":
            embed.add_field(name=f"{LocationI}Região do server:", value=f"🇷🇺 ``{Region}``")
        else:
            embed.add_field(name=f"{LocationI}Região do Server:", value=f"``{str(ctx.guild.region)}``")

        await ctx.send(embed=embed)

    @_info.command(aliases=["cargo"], usage="[p]info [cargo] [Role: Mention/ID]")
    @commands.guild_only()
    async def role(self, ctx, role: discord.Role=None):
        if role is None:
            return await ctx.send(embed=discord.Embed(description="Favor informe um cargo.").set_footer(text="[p]info [Cargo: Menção/ID]"))

        perms = role.permissions
        permissões = ["role.mentionable", "role.hoist", "perms.administrator", "perms.ban_members", "perms.kick_members",
                    "perms.change_nickname", "perms.connect", "perms.create_instant_invite", "perms.deafen_members",
                    "perms.embed_links", "perms.external_emojis", "perms.manage_channels", "perms.manage_emojis",
                    "perms.manage_messages", "perms.manage_nicknames", "perms.manage_roles", "perms.manage_guild",
                    "perms.mention_everyone", "perms.move_members", "perms.mute_members", "perms.read_message_history",
                    "perms.send_messages", "perms.speak", "perms.use_voice_activation", "perms.manage_webhooks", "perms.add_reactions"]

        finalt = []
        finalf = []

        for x in permissões:
            if eval(x) is True:
                finalt.append(x.replace("perms.", "+ ").replace("role.", "+ "))
            else:
                finalf.append(x.replace("perms.", "- ").replace("role.", "- "))

        a = "\n".join(finalt)
        b = "\n".join(finalf)

        count = len([member for member in ctx.guild.members if discord.utils.get(member.roles, name=role.name)])
        await ctx.send(f">>> ```diff\nName    : {role.name}\nMembers : {count}\n\n{a}\n{b}```")

    @_info.command(name="filme", aliases=["film"], description="Ver informações do filme que deseja pelo OMdb.", usage="[p]info filme [Nome do Filme]")
    @commands.guild_only()
    async def film(self, ctx, *, film:str=None):
        if film is None:
            return ctx.send(embed=discord.Embed(description=f"{ImdbI} Favor informar o filme.", color=0xc63939).set_footer(text="Modo de uso: [p]info filme [Nome do Filme]"), delete_after=30)
        
        request_code, request_status = await self.request.omdb(film=film)
        if not request_status == 200:
            return ctx.send(embed=discord.Embed(description=f"{ImdbI} API Indisponível no momento!", color=0xc63939), delete_after=30)

        genre = str(request_code["Genre"]) \
        .replace("Horror", f"{HorrorI}Terror") \
        .replace("Animation", f"{AnimationI}Animação") \
        .replace("Adventure", f"{AdventureI}Aventura") \
        .replace("Art cinema", "Cinema de arte") \
        .replace("Stained", "Manchado") \
        .replace("Catastrophe cinema", "Cinema catástrofe") \
        .replace("Action", f"{ActionI}Ação") \
        .replace("Comedy", f"{ComedyI}Comédia") \
        .replace("Romantic comedy", f"{ComedyI}Comédia romântica") \
        .replace("Dramatic comedy", f"{DramaI}Comédia dramática") \
        .replace("Dance", f"{MusicalI}Dança") \
        .replace("Documentary", f"{DocumentaryI}Documentário") \
        .replace("Docufiction", f"{ScifiI}Docuficção") \
        .replace("Drama", f"{DramaI}Drama") \
        .replace("Espionage", f"{SpyI}Espionagem") \
        .replace("Sci-Fi", f"{ScifiI}Ficção científica") \
        .replace("War Movies", f"{WarI}Guerra") \
        .replace("Musical", f"{MusicalI}Músical") \
        .replace("Police movie", f"{AgentI}Policial") \
        .replace("Romance", f"{RomanceI}Romance") \
        .replace("Sitcom", "Seriado") \
        .replace("Thriller", f"{ThrillerI}Suspense")

        GeneroI = str(request_code["Genre"]) \
        .replace("Horror", f"{HorrorI}") \
        .replace("Animation", f"{AnimationI}") \
        .replace("Adventure", f"{AdventureI}") \
        .replace("Action", f"{ActionI}") \
        .replace("Comedy", f"{ComedyI}") \
        .replace("Romantic comedy", f"{ComedyI}") \
        .replace("Dramatic comedy", f"{DramaI}") \
        .replace("Dance", f"{MusicalI}") \
        .replace("Documentary", f"{DocumentaryI}") \
        .replace("Docufiction", f"{ScifiI}") \
        .replace("Drama", f"{DramaI}") \
        .replace("Espionage", f"{SpyI}") \
        .replace("Sci-Fi", f"{ScifiI}") \
        .replace("War Movies", f"{WarI}") \
        .replace("Musical", f"{MusicalI}") \
        .replace("Police movie", f"{AgentI}") \
        .replace("Romance", f"{RomanceI}") \
        .replace("Thriller", f"{ThrillerI}")

        embed = discord.Embed(title=f"{ImdbI} JrFilme - {str(request_code['Title'])}", color=0xff0000, datetime=datetime.utcnow())
        embed.add_field(name=f"{GeneroI}Genêro(s):", value=str(genre))
        embed.add_field(name=f"{TimeI}Tempo:", value=str(request_code["Runtime"]))
        embed.add_field(name=f"{CalendarI}Ano:", value=str(request_code["Year"]))
        embed.add_field(name=f"{DirectorI}Diretor:", value=str(request_code["Director"]))
        embed.add_field(name=f"{ActorsI}Atores:", value=str(request_code["Actors"]))
        embed.add_field(name=f"{ReportCardI}Nota(s):", value=str(request_code["imdbRating"]))
        embed.set_thumbnail(url=str(request_code["Poster"]))
        embed.set_footer(text=str(request_code["Production"]), icon_url=ctx.author.avatar_url)

        ctx.send(embed=embed)

    @_info.command(name="clima", aliases=["weather"])
    @commands.guild_only()
    async def weather(self, ctx, *, location:str=None):
        if location is None:
            return await ctx.send(embed=discord.Embed(description=f"{WeatherMapI}Por favor informe o país, estado ou cidade.", color=0xef0027), delete_after=30)

        request_code, request_status = await self.request.weather(location)

        if int(request_code["cod"]) == 404:
            return await ctx.send(embed=discord.Embed(description=f"{WeatherMapI}Não encontrei nenhum lugar com este nome 😟", color=0xef0027), delete_after=30)

        nome        = str(request_code["name"])
        description = str(request_code["weather"][0]["description"])
        clima       = str(request_code["weather"][0]["main"])
        umidade     = str(request_code["main"]["humidity"])
        temperatura = int(request_code["main"]["temp"] - 273.15)
        velocidade  = int(request_code["wind"]["speed"])
        pais        = str(request_code["sys"]["country"])
        longitude   = str(request_code["coord"]["lon"])
        latitude    = str(request_code["coord"]["lat"])

        embed = discord.Embed(title=f"{WeatherMapI}OpenWeatherMap - {nome}", color=50175, timestamp=datetime.utcnow())
        embed.add_field(name=f"{NameI}Nome:", value=f"**```{nome}```**")

        if clima == "Rain":
            embed.add_field(name=f"{RainI}Clima:", value=f"**```Chuva```**")
        elif clima == "Clouds":
            embed.add_field(name=f"{CloudyI}Clima:", value=f"**```Nuvens```**")
        elif clima == "Fog":
            embed.add_field(name=f"{FogI}Clima:", value=f"**```Névoa```**")
        elif clima == "Clear":
            embed.add_field(name=f"{ClearI}Clima:", value=f"**```Limpo```**")
        elif clima == "Drizzle":
            embed.add_field(name=f"{DrizzleI}Clima:", value=f"**```Chuvisco```**")
        elif clima == "Storm":
            embed.add_field(name=f"{StormI}Clima:", value=f"**```Tempestade```**")
        else:
            embed.add_field(name="Clima:", value=f"**```{clima}```**")

        embed.add_field(name=f"{MoistureI}Umidade:", value=f"**```{umidade}%```**")
        embed.add_field(name=f"{SpeedI}Velocidade:", value=f"**```{velocidade} KM/H```**")

        if pais == "BR":
            embed.add_field(name="🇧🇷Pais:", value="**```Brasil```**")
        elif pais == "US":
            embed.add_field(name="🇺🇸Pais:", value="**```USA```**")
        elif pais == "RU":
            embed.add_field(name="🇷🇺Pais:", value="**```Russia```**")
        elif pais == "AR":
            embed.add_field(name="🇦🇷Pais:", value="**```argentina```**")
        else:
            embed.add_field(name="Pais:", value=f"**```{pais}```**")

        embed.add_field(name=f"{CoordeI}Coordenadas:", value=f"**```{longitude}/{latitude}```**")
        embed.add_field(name=f"{TempI}Temperatura:", value=f"**```{temperatura}ºC```**")
        embed.set_footer(text=f"Pedido por: {ctx.author.name}")
        await ctx.send(embed=embed)

    @commands.command(aliases=["news"])
    @commands.guild_only()
    async def noticias(self, ctx):
        request_code, request_status = await self.request.news()
        random_result = randint(0, int(request_code["totalResults"]))

        author      = str(request_code["articles"][int(random_result)]["author"]).replace("None", "Google News (Brasil)")
        titulo      = str(request_code["articles"][int(random_result)]["title"])
        description = str(request_code["articles"][int(random_result)]["description"]).replace("None", "Sem descrição.")
        url         = str(request_code["articles"][int(random_result)]["url"])
        data        = str(request_code["articles"][int(random_result)]["publishedAt"])
        img         = str(request_code["articles"][int(random_result)]["urlToImage"])

        embed = discord.Embed(title=f"{NewsI} JrNews - Notícias", color=0xFF4040, timestamp=datetime.utcnow())
        embed.add_field(name=f"{WriterI}**Autor:**", value=f"**```{author}```**")
        embed.add_field(name=f"{TitleI}**Título:**", value=f"**```{titulo}```**")
        embed.add_field(name=f"{DescI}**Descrição:**", value=f"**```{description}```{LinkI}Url da notícia:** [**`Link`**]({url})")
        embed.set_footer(text=f"Data: {data[:10]} | Hora: {data[11:][:5]}", icon_url="https://i.imgur.com/YIKnKoW.png")
        embed.set_thumbnail(url=img)
        await ctx.send(embed=embed)

    @commands.command(aliases=["wiki", "wkpd"])
    @commands.guild_only()
    async def wikipedia(self, ctx, *, query:str=None):
        if query is None:
            return await ctx.send(embed=discord.Embed(description=f"{WikiI}Você não informou o que deseja...", color=0xef0027), delete_after=30)

        try:
            q = wikipedia.page(query)
            wikipedia.set_lang("pt")
            summary = wikipedia.summary(query, sentences=5)
            await ctx.send(embed=discord.Embed(title=f"{WikiI}Wikipédia - {query}", description=f"**```{summary}```**\nPara mais informações [**clique aqui**]({q.url})", color=0x2196f3))
        except wikipedia.exceptions.PageError:
            await ctx.send(embed=discord.Embed(description=f"{WikiI}Poxa :/ Não consegui encontrar nada com este título.", color=0xef0027), delete_after=30)

def setup(client):
    client.add_cog(MyInformation(client))