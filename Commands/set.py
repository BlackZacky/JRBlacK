from discord.ext import commands
from Database import *

import discord

WelI     = "<:welcome:572480320344162325>"
HddI     = "<:hdd:571174665121169418>"
HintI    = "<:hint:571396019322093580>"
LogsI    = "<:logs:572463446487072778>"
MongoDBI = "<:mongodb:571423025216487435>"
CounterI = "<:counter:572481181086646292>"
ScienceI = "<:sciencefiction:572482102633824265>"
SilenceI = "<:silence:572483419389427723>"
ErrorI   = "<:error:643891624878800896>"

class MySet(commands.Cog, name="Setar"):
    def __init__(self, client):
        self.client = client
        self.check  = database.check()
        self.guild  = database.guild()
        self.user   = database.user()
        self.json    = {
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

    @commands.group(name="setar", aliases=["set"], usage="[p]setar [sub comando]", no_pm=True)
    async def _Set(self, ctx):
        if ctx.invoked_subcommand is None:
            if self.guild.get_whitelist(ctx.guild.id) == ctx.channel.id or self.guild.get_whitelist(ctx.guild.id) == 0:
                return await self.sub_commands(ctx, ctx.command.name)
            else:
                 return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention}, você não pode executar comandos nesse chat.", color=0xef0027), delete_after=15)

    @_Set.command()
    async def background(self, ctx, *, x:str=None):
        if self.guild.get_whitelist(ctx.guild.id) == ctx.channel.id or self.guild.get_whitelist(ctx.guild.id) == 0:
            backgroundP = {"background 1":{
                            "ID":154,
                            "Url":"https://i.imgur.com/nhEfmIY.jpg"
                            },
                        "background 2":{
                            "ID":413,
                            "Url":"https://i.imgur.com/UM0icxL.jpg"
                            },
                        "background 3":{
                            "ID":456,
                            "Url":"https://i.imgur.com/7Lg3aRy.jpg"
                            },                            
                        "background 4":{
                            "ID":867,
                            "Url":"https://i.imgur.com/M1SEbiF.jpg"
                            },
                        "background 5":{
                            "ID":345,
                            "Url":"https://i.imgur.com/8zNOkSC.jpg"
                            },
                        "background 6":{
                            "ID":978,
                            "Url":"https://i.imgur.com/2ys3opI.jpg"
                            }
                        }

            if x is None:
                if "False" == self.user.get_background(ctx.guild.id, ctx.author.id):
                    return await ctx.send(embed=discord.Embed(description=f"{ErrorI} Este background já está definido.", color=0xef0027))

                self.user.post_background(ctx.guild.id, ctx.author.id, "False")
                return await ctx.send(embed=discord.Embed(description=f"O seu background foi alterado para o ``background padrão``", color=0x6600db))
            elif backgroundP[x.lower()]["Url"] == self.user.get_background(ctx.guild.id, ctx.author.id):
                return await ctx.send(embed=discord.Embed(description=f"{ErrorI} Este background já está definido.", color=0xef0027))
            elif x.lower() in list(backgroundP):
                self.user.post_background(ctx.guild.id, ctx.author.id, backgroundP[x.lower()]["Url"])
                return await ctx.send(embed=discord.Embed(description=f"O seu background foi alterado para o ``{x}``", color=0x6600db).set_image(url=backgroundP[x.lower()]["Url"]))
            else:
                return await ctx.send(embed=discord.Embed(description=f"{ErrorI} O background que você informou não existe.", color=0xef0027))
        else:
             return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention}, você não pode executar comandos nesse chat.", color=0xef0027), delete_after=15)

    @commands.bot_has_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    @_Set.command(name="economia", aliases=["economy"], no_pm=True)
    async def economy(self, ctx):
        if self.guild.get_whitelist(ctx.guild.id) == ctx.channel.id or self.guild.get_whitelist(ctx.guild.id) == 0:
            if self.check.guild(ctx.guild.id) is False:
                return await ctx.send(embed=discord.Embed(description=f"**{MongoDBI} {ctx.author.mention}, você precisa configurar o servidor na database.**", color=0xef0027))

            if self.guild.get_systemEconomy(ctx.guild.id) == "True":
                self.guild.post_systemEconomy(ctx.guild.id)
                return await ctx.send(embed=discord.Embed(description=f"Sistema de _economia_ do servidor foi **desativado**.", color=0xef0027))

            self.guild.post_systemEconomy(ctx.guild.id)
            await ctx.send(embed=discord.Embed(description=f"Sistema de _economia_ do servidor foi **ativado**.", color=0x00ef5b))
        else:
             return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention}, você não pode executar comandos nesse chat.", color=0xef0027), delete_after=15)

    @commands.bot_has_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    @_Set.command(name="xplevel", aliases=["xp", "level"], no_pm=True)
    async def xplevel(self, ctx):
        if self.guild.get_whitelist(ctx.guild.id) == ctx.channel.id or self.guild.get_whitelist(ctx.guild.id) == 0:
            if self.check.guild(ctx.guild.id) is False:
                return await ctx.send(embed=discord.Embed(description=f"**{MongoDBI} {ctx.author.mention}, você precisa configurar o servidor na database.**", color=0xef0027))

            if self.guild.get_systemXpLevel(ctx.guild.id) == "True":
                self.guild.post_systemXpLevel(ctx.guild.id)
                return await ctx.send(embed=discord.Embed(description=f"Sistema de _Xp/Level_ do servidor foi **desativado**.", color=0xef0027))

            self.guild.post_systemXpLevel(ctx.guild.id)
            await ctx.send(embed=discord.Embed(description=f"Sistema de _Xp/Level_ do servidor foi **ativado**.", color=0x00ef5b))
        else:
             return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention}, você não pode executar comandos nesse chat.", color=0xef0027), delete_after=15)

    @_Set.command(name="sobre", aliases=["about"], no_pm=True)
    async def _About(self, ctx, *, about:str="Sem descrição."):
        if self.guild.get_whitelist(ctx.guild.id) == ctx.channel.id or self.guild.get_whitelist(ctx.guild.id) == 0:
            self.user.post_about(ctx.guild.id, ctx.author.id, about)
            await ctx.send(embed=discord.Embed(description=f"**Sobre alterado:** {about}", color=0x00ef5b))
        else:
             return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention}, você não pode executar comandos nesse chat.", color=0xef0027), delete_after=15)

    @_Set.command(name="auto-reação", aliases=["autoreacao", "autoreaçao", "autoreação", "reaçao", "reação", "auto-react"])
    @commands.bot_has_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()
    async def autoreact(self, ctx, channel:discord.TextChannel=None):
        if self.guild.get_whitelist(ctx.guild.id) == ctx.channel.id or self.guild.get_whitelist(ctx.guild.id) == 0:
            if self.check.guild(ctx.guild.id) is False:
                return await ctx.send(embed=discord.Embed(description=f"**{MongoDBI} Me parece que seu servidor não está configurado na minha database. COMMAND: @Me!?**", color=0xef0027))
            if channel is None:
                self.guild.post_autoReact(ctx.guild.id, 0)
                return await ctx.send(embed=discord.Embed(description=f"**{HintI} _Auto-React_ desativada!**", color=0xef0027))

            self.guild.post_autoReact(ctx.guild.id, channel.id)
            await ctx.send(embed=discord.Embed(description=f"**{HintI} _Auto-React_ ativada no canal: {channel.mention}!**", color=0x00ef5b))
        else:
             return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention}, você não pode executar comandos nesse chat.", color=0xef0027), delete_after=15)

    @_Set.command(name="logs")
    @commands.bot_has_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()
    async def logs(self, ctx, channel:discord.TextChannel=None):
        if self.guild.get_whitelist(ctx.guild.id) == ctx.channel.id or self.guild.get_whitelist(ctx.guild.id) == 0:
            if self.check.guild(ctx.guild.id) is False:
                return await ctx.send(embed=discord.Embed(description=f"**{MongoDBI} Me parece que seu servidor não está configurado na minha database. COMMAND: @Me!?**", color=0xef0027))
            if channel is None:
                self.guild.post_logs(ctx.guild.id, 0)
                return await ctx.send(embed=discord.Embed(description=f"**{LogsI} _Logs_ desativado!**", color=0xef0027))
            
            self.guild.post_logs(ctx.guild.id, channel.id)
            await ctx.send(embed=discord.Embed(description=f"**{LogsI} _Logs_ ativado no canal: {channel.mention}!**", color=0x00ef5b))
        else:
             return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention}, você não pode executar comandos nesse chat.", color=0xef0027), delete_after=15)

    @_Set.command(name="bem-vindo", aliases=["welcome", "wel", "bemvindo"])
    @commands.bot_has_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()
    async def welcome(self, ctx, channel:discord.TextChannel=None):
        if self.guild.get_whitelist(ctx.guild.id) == ctx.channel.id or self.guild.get_whitelist(ctx.guild.id) == 0:
            if self.check.guild(ctx.guild.id) is False:
                return await ctx.send(embed=discord.Embed(description=f"**{MongoDBI} Me parece que seu servidor não está configurado na minha database. COMMAND: @Me!?**", color=0xef0027))
            if channel is None:
                self.guild.post_welcome(ctx.guild.id, 0)
                return await ctx.send(embed=discord.Embed(description=f"**{WelI} _Welcome_ desativado!**", color=0xef0027))
            
            self.guild.post_welcome(ctx.guild.id, channel.id)
            await ctx.send(embed=discord.Embed(description=f"**{WelI} _Welcome_ ativado no canal: {channel.mention}!**", color=0x00ef5b))
        else:
             return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention}, você não pode executar comandos nesse chat.", color=0xef0027), delete_after=15)

    @_Set.command(name="disco-rigido", aliases=["disco", "rigido", "harddisk"])
    @commands.bot_has_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()
    async def hard(self, ctx, channel:discord.TextChannel=None):
        if self.guild.get_whitelist(ctx.guild.id) == ctx.channel.id or self.guild.get_whitelist(ctx.guild.id) == 0:
            if self.check.guild(ctx.guild.id) is False:
                return await ctx.send(embed=discord.Embed(description=f"**{MongoDBI} Me parece que seu servidor não está configurado na minha database. COMMAND: @Me!?**", color=0xef0027))
            if channel is None:
                self.guild.post_harddisk(ctx.guild.id, 0)
                return await ctx.send(embed=discord.Embed(description=f"**{HddI} _Harddisk_ desativado!**", color=0xef0027))

            self.guild.post_harddisk(ctx.guild.id, channel.id)
            await ctx.send(embed=discord.Embed(description=f"**{HddI} _Harddisk_ ativado no canal: {channel.mention}!**", color=0x00ef5b))
        else:
             return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention}, você não pode executar comandos nesse chat.", color=0xef0027), delete_after=15)

    @_Set.command(name="disco-rigido-2", aliases=["disco2", "rigido2", "harddisk2"])
    @commands.bot_has_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()
    async def hard2(self, ctx, channel:discord.TextChannel=None):
        if self.guild.get_whitelist(ctx.guild.id) == ctx.channel.id or self.guild.get_whitelist(ctx.guild.id) == 0:
            if self.check.guild(ctx.guild.id) is False:
                return await ctx.send(embed=discord.Embed(description=f"**{MongoDBI} Me parece que seu servidor não está configurado na minha database. COMMAND: @Me!?**", color=0xef0027))
            if channel is None:
                self.guild.post_harddisk2(ctx.guild.id, 0)
                return await ctx.send(embed=discord.Embed(description=f"**{HddI} _Harddisk 2_ desativado!**", color=0xef0027))

            self.guild.post_harddisk2(ctx.guild.id, channel.id)
            await ctx.send(embed=discord.Embed(description=f"**{HddI} _Harddisk 2_ ativado no canal: {channel.mention}!**", color=0x00ef5b))
        else:
             return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention}, você não pode executar comandos nesse chat.", color=0xef0027), delete_after=15)

    @_Set.command(name="disco-rigido-3", aliases=["disco3", "rigido3", "harddisk3"])
    @commands.bot_has_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()
    async def hard3(self, ctx, channel:discord.TextChannel=None):
        if self.guild.get_whitelist(ctx.guild.id) == ctx.channel.id or self.guild.get_whitelist(ctx.guild.id) == 0:
            if self.check.guild(ctx.guild.id) is False:
                return await ctx.send(embed=discord.Embed(description=f"**{MongoDBI} Me parece que seu servidor não está configurado na minha database. COMMAND: @Me!?**", color=0xef0027))
            if channel is None:
                self.guild.post_harddisk3(ctx.guild.id, 0)
                return await ctx.send(embed=discord.Embed(description=f"**{HddI} _Harddisk 3_ desativado!**", color=0xef0027))

            self.guild.post_harddisk3(ctx.guild.id, channel.id)
            await ctx.send(embed=discord.Embed(description=f"**{HddI} _Harddisk 3_ ativado no canal: {channel.mention}!**", color=0x00ef5b))
        else:
             return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention}, você não pode executar comandos nesse chat.", color=0xef0027), delete_after=15)

    @_Set.command(name="contador", aliases=['counter'])
    @commands.bot_has_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()
    async def counter(self, ctx, channel: discord.TextChannel=None):
        if self.guild.get_whitelist(ctx.guild.id) == ctx.channel.id or self.guild.get_whitelist(ctx.guild.id) == 0:
            if self.check.guild(ctx.guild.id) is False:
                return await ctx.send(embed=discord.Embed(description=f"**{MongoDBI} Me parece que seu servidor não está configurado na minha database. COMMAND: @Me!?**", color=0xef0027))
            if channel is None:
                await self.client.get_channel(self.guild.get_counter(ctx.guild.id)).edit(topic="")
                self.guild.post_counter(ctx.guild.id, 0)
                return await ctx.send(embed=discord.Embed(description=f"**{CounterI} _Contador_ desativado!**", color=0xef0027))

            self.guild.post_counter(ctx.guild.id, channel.id)
            
            text = str(len(ctx.guild.members))
            for n in range(0, 10):
                text = text.replace(str(n), f"E{n}")
            for n in range(0, 10):
                text = text.replace(f"E{n}", self.json[f"E{n}"])                                                  

            await self.client.get_channel(channel.id).edit(topic=f'Membros: {text}')

            await ctx.send(embed=discord.Embed(description=f"**{CounterI} _Contador_ ativado no canal: {channel.mention}!**", color=0x00ef5b))
        else:
             return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention}, você não pode executar comandos nesse chat.", color=0xef0027), delete_after=15)

    @_Set.command(name="auto-role", aliases=['autorole'])
    @commands.bot_has_permissions(manage_messages=True, manage_roles=True)
    @commands.has_permissions(manage_messages=True, manage_roles=True)
    @commands.guild_only()
    async def autorole(self, ctx, role: discord.Role=None):
        if self.guild.get_whitelist(ctx.guild.id) == ctx.channel.id or self.guild.get_whitelist(ctx.guild.id) == 0:
            if self.check.guild(ctx.guild.id) is False:
                return await ctx.send(embed=discord.Embed(description=f"**{MongoDBI} Me parece que seu servidor não está configurado na minha database. COMMAND: @Me!?**", color=0xef0027))
            if role is None:
                self.guild.post_autoRole(ctx.guild.id, 0)
                return await ctx.send(embed=discord.Embed(description=f"**{ScienceI} _Auto-Role_ desativado!**", color=0xef0027))

            self.guild.post_autoRole(ctx.guild.id, role.id)
            await ctx.send(embed=discord.Embed(description=f"**{ScienceI} _Auto-Role_ ativado no cargo: {role.name}!**", color=0x00ef5b))
        else:
             return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention}, você não pode executar comandos nesse chat.", color=0xef0027), delete_after=15)

    @_Set.command(name="mute-role", aliases=['muterole'])
    @commands.bot_has_permissions(manage_roles=True)
    @commands.has_permissions(manage_roles=True)
    @commands.guild_only()
    async def muterole(self, ctx, role:discord.Role=None):
        if self.guild.get_whitelist(ctx.guild.id) == ctx.channel.id or self.guild.get_whitelist(ctx.guild.id) == 0:
            if self.check.guild(ctx.guild.id) is False:
                return await ctx.send(embed=discord.Embed(description=f"**{MongoDBI} Me parece que seu servidor não está configurado na minha database. COMMAND: @Me!?**", color=0xef0027))
            if role is None:
                self.guild.post_muteRole(ctx.guild.id, 0)
                return await ctx.send(embed=discord.Embed(description=f"**{SilenceI} _Mute-Role_ desativado!**", color=0xef0027))

            self.guild.post_muteRole(ctx.guild.id, role.id)
            await ctx.send(embed=discord.Embed(description=f"**{SilenceI} _Mute-Role_ ativado no cargo: {role.name}!**", color=0x00ef5b))
        else:
             return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention}, você não pode executar comandos nesse chat.", color=0xef0027), delete_after=15)

    @_Set.command(name="lista-branca", aliases=['listabranca', 'whitelist', 'whitel', 'lb', 'wl'])
    @commands.bot_has_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()
    async def whitelist(self, ctx, channel:discord.TextChannel=None):
        if self.guild.get_whitelist(ctx.guild.id) == ctx.channel.id or self.guild.get_whitelist(ctx.guild.id) == 0:
            if self.check.guild(ctx.guild.id) is False:
                return await ctx.send(embed=discord.Embed(description=f"**{MongoDBI} Me parece que seu servidor não está configurado na minha database. COMMAND: @Me!?**", color=0xef0027))
            if channel is None:
                self.guild.post_whitelist(ctx.guild.id, 0)
                return await ctx.send(embed=discord.Embed(description=f"**{SilenceI} _Whitelist_ desativada!**", color=0xef0027))

            self.guild.post_whitelist(ctx.guild.id, channel.id)
            await ctx.send(embed=discord.Embed(description=f"**{SilenceI} _Whitelist_ ativada no canal: {channel.name}!**", color=0x00ef5b))
        else:
             return await ctx.send(embed=discord.Embed(description=f"{ctx.author.mention}, você não pode executar comandos nesse chat.", color=0xef0027), delete_after=15)

def setup(client):
    client.add_cog(MySet(client))