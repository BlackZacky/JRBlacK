from discord.ext.commands import errors
from discord.ext import commands

import discord, asyncio

class MyHandler(commands.Cog, name="Handler Error"):
    def __init__(self, bot):
        self.bot = bot

    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, "on_error"):
            return

        error = getattr(error, "original", error)

        if isinstance(error, commands.CommandNotFound):
            return await ctx.message.add_reaction("❌")

        if isinstance(error, commands.DisabledCommand):
            return await ctx.send("```asciidoc\nCommands :: Este comando está desabilitado!```")

        if isinstance(error, commands.UserInputError):
            await ctx.send(f"```asciidoc\nInput :: Entrada inválida```")
            
            command_usage = self.bot.get_command(ctx.command.name).usage
            if command_usage is None:
                command_usage = "Este comando não possui um tutorial de uso."
            
            return await ctx.send(f"""```asciidoc\n[Comando {ctx.command.name}]\n Modo de uso    :: {command_usage}```""")

        if isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send("```asciidoc\nPrivate :: Este comando não é permitido em privado/direct message```")
            except discord.Forbidden:
                pass
            return

        if isinstance(error, commands.BotMissingPermissions):
            missing = [perm.replace("_", " ").replace("guild", "server").title() for perm in error.missing_perms]
            if len(missing) > 2:
                fmt = "{}, e {}".format(", ".join(missing[:-1]), missing[-1])
            else:
                fmt = " e ".join(missing)
            return await ctx.send(f"```asciidoc\nPermissions :: Eu preciso da(s) {fmt} permissão(s) para usar este comando.```")

        if isinstance(error, commands.MissingPermissions):
            missing = [perm.replace("_", " ").replace("guild", "server").title() for perm in error.missing_perms]
            if len(missing) > 2:
                fmt = "{}, e {}".format(", ".join(missing[:-1]), missing[-1])
            else:
                fmt = " e ".join(missing)
            return await ctx.send(f"```asciidoc\nPermissions :: Você precisa da(s) {fmt} permissão(s) para usar este comando.```")
        
        if isinstance(error, commands.NotOwner):
            return await ctx.send(f"```asciidoc\nPermissions :: {ctx.author} você não tem permissão para fazer o uso deste comando.```")

        if isinstance(error, commands.CheckFailure):
            pass

def setup(bot):
    bot.add_cog(MyHandler(bot))
    bot.add_listener(MyHandler(bot).on_command_error)