async def sub_commands(client, ctx, command):
    lista = []
    for x in client.get_command(command).all_commands:
        if client.get_command(f"{command} {x}").name is x:
            lista.append(x)

    x = "".join(lista)
    if len(lista) > 1:
        x = " | ".join(lista)

    return await ctx.send(f"""```asciidoc
[Comando {command}]
  Modo de uso    :: {client.get_command(command).usage}
  Sub Comando(s) :: {x}
```""")