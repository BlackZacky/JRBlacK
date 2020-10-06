from Commands.Utils.icons import getIcon
from discord.ext import commands
from discord.ext import menus
from Database import *

import discord

i_gunStore      = getIcon("Weapons Store")
i_store         = getIcon("Store")
i_wallpaper     = getIcon("Image")
i_wallet        = getIcon("Wallet")
i_back          = getIcon("Back")
i_close         = getIcon("Close")
i_M1911         = getIcon("M1911")
i_M4            = getIcon("M4A1")
i_GLOCK         = getIcon("GLOCK")
i_AK47          = getIcon("AK47")
i_storeError    = getIcon("Store Error")
i_gunStoreError = getIcon("Weapons Store Error")

class MyMenuStore(menus.Menu):
    def __init__(self):
        super().__init__(timeout=30.0, delete_message_after=True)
        self.result = None

    async def send_initial_message(self, ctx, channel):
        return await channel.send(embed=discord.Embed(title=f"{i_store} Store - {ctx.guild.name}", color=0x6600db, description=f"""
            ``Papel de parede ​:`` {i_wallpaper}
            ``Armas​ ​​ ​​      ​​ ​​​​ ​​​ ​​:`` {i_gunStore}
    ⠀
            ``Comprar​ ​​      ​​ ​​ ​:`` {i_wallet}
            ``Fechar​      ​​ ​​ ​​ ​​ ​:`` {i_close}"""))

    @menus.button(i_gunStore)
    async def on_weapons(self, payload):
        embed = discord.Embed(title=f"{i_gunStore} Store - Armas", color=0x6600db)
        embed.add_field(name="Glock", value=f"**ID:** 279\n**Preço:** R$60000\n**Ícone:** {i_GLOCK}")
        embed.add_field(name="M1911", value=f"**ID:** 191\n**Preço:** R$70000\n**Ícone:** {i_M1911}")
        embed.add_field(name="AK-47", value=f"**ID:** 762\n**Preço:** R$110000\n**Ícone:** {i_AK47}")
        embed.add_field(name="M4", value=f"**ID:** 556\n**Preço:** R$115000\n**Ícone:** {i_M4}")
        await self.message.edit(embed=embed)
        
        self.result = False
        
    @menus.button(i_wallpaper)
    async def on_wallpaper(self, payload):
        embed = discord.Embed(title=f"{i_wallpaper} Store - Papel de Parede", color=0x6600db)
        embed.add_field(name="Background 1", value="**ID:** 154\n**Preço:** R$10000\n**Papel de Parede:** [**Clique aqui**](https://i.imgur.com/nhEfmIY.jpg)")
        embed.add_field(name="Background 2", value="**ID:** 413\n**Preço:** R$12000\n**Papel de Parede:** [**Clique aqui**](https://i.imgur.com/UM0icxL.jpg)")
        embed.add_field(name="Background 3", value="**ID:** 456\n**Preço:** R$13000\n**Papel de Parede:** [**Clique aqui**](https://i.imgur.com/7Lg3aRy.jpg)")
        embed.add_field(name="Background 4", value="**ID:** 867\n**Preço:** R$14000\n**Papel de Parede:** [**Clique aqui**](https://i.imgur.com/M1SEbiF.jpg)")
        embed.add_field(name="Background 5", value="**ID:** 345\n**Preço:** R$15000\n**Papel de Parede:** [**Clique aqui**](https://i.imgur.com/8zNOkSC.jpg)")
        embed.add_field(name="Background 6", value="**ID:** 978\n**Preço:** R$16000\n**Papel de Parede:** [**Clique aqui**](https://i.imgur.com/2ys3opI.jpg)")
        await self.message.edit(embed=embed)
        
        self.result = False

    @menus.button(i_wallet)
    async def on_atm(self, payload):
        self.result = True
        self.stop()

    @menus.button(i_close)
    async def on_exit(self, payload):
        self.result = False
        self.stop()

    async def prompt(self, ctx):
        await self.start(ctx, wait=True)
        return self.result

class MyStore(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.user  = database.user()
        self.guild = database.guild()
        self.check = database.check()

    @commands.command(name="loja", aliases=["store"])
    async def store(self, ctx):
        menu = await MyMenuStore().prompt(ctx)
        if menu:
            def check_author_message(message):
                return message.author == ctx.author and message.channel == ctx.channel

            message = await ctx.send(embed=discord.Embed(color=0x00ef5b, description=f"{i_wallet} Qual o ID do item/papel de parede/arma que deseja ?"))
            try:
                message_author = await self.client.wait_for('message', check=check_author_message, timeout=300.0)
            except TimeoutError:
                return await message.delete()

            if message_author.content == "154":
                if "Background 1" in self.user.get_inventory_background(ctx.guild.id, ctx.author.id):
                    return await message.edit(embed=discord.Embed(color=0xef0027, description=f"{i_storeError} Você já tem este **papel de parede**."))
                if not self.user.get_money_hand(ctx.guild.id, ctx.author.id) >= 10000:
                    return await message.edit(embed=discord.Embed(color=0xef0027, description=f"{i_storeError} Dinheiro insuficiente para comprar este papel de parede."))
                
                self.user.post_money_hand(ctx.guild.id, ctx.author.id, -10000)
                self.user.post_inventory_background(ctx.guild.id, ctx.author.id, "Background 1")
                return await ctx.send(embed=discord.Embed(color=0x00ef5b, description=f"{i_store} Compra efetuada com sucesso!"), delete_after=300.0)

            elif message_author.content == "413":
                if "Background 2" in self.user.get_inventory_background(ctx.guild.id, ctx.author.id):
                    return await message.edit(embed=discord.Embed(color=0xef0027, description=f"{i_storeError} Você já tem este **papel de parede**."))
                if not self.user.get_money_hand(ctx.guild.id, ctx.author.id) >= 12000:
                    return await message.edit(embed=discord.Embed(color=0xef0027, description=f"{i_storeError} Dinheiro insuficiente para comprar este papel de parede."))

                self.user.post_money_hand(ctx.guild.id, ctx.author.id, -12000)
                self.user.post_inventory_background(ctx.guild.id, ctx.author.id, "Background 2")
                return await ctx.send(embed=discord.Embed(color=0x00ef5b, description=f"{i_store} Compra efetuada com sucesso!"), delete_after=300.0)

            elif message_author.content == "456":
                if "Background 3" in self.user.get_inventory_background(ctx.guild.id, ctx.author.id):
                    return await message.edit(embed=discord.Embed(color=0xef0027, description=f"{i_storeError} Você já tem este **papel de parede**."))
                if not self.user.get_money_hand(ctx.guild.id, ctx.author.id) >= 13000:
                    return await message.edit(embed=discord.Embed(color=0xef0027, description=f"{i_storeError} Dinheiro insuficiente para comprar este papel de parede."))

                self.user.post_money_hand(ctx.guild.id, ctx.author.id, -13000)
                self.user.post_inventory_background(ctx.guild.id, ctx.author.id, "Background 3")
                return await ctx.send(embed=discord.Embed(color=0x00ef5b, description=f"{i_store} Compra efetuada com sucesso!"), delete_after=300.0)

            elif message_author.content == "867":
                if "Background 4" in self.user.get_inventory_background(ctx.guild.id, ctx.author.id):
                    return await message.edit(embed=discord.Embed(color=0xef0027, description=f"{i_storeError} Você já tem este **papel de parede**."))
                if not self.user.get_money_hand(ctx.guild.id, ctx.author.id) >= 14000:
                    return await message.edit(embed=discord.Embed(color=0xef0027, description=f"{i_storeError} Dinheiro insuficiente para comprar este papel de parede."))

                self.user.post_money_hand(ctx.guild.id, ctx.author.id, -14000)
                self.user.post_inventory_background(ctx.guild.id, ctx.author.id, "Background 4")
                return await ctx.send(embed=discord.Embed(color=0x00ef5b, description=f"{i_store} Compra efetuada com sucesso!"), delete_after=300.0)

            elif message_author.content == "345":
                if "Background 5" in self.user.get_inventory_background(ctx.guild.id, ctx.author.id):
                    return await message.edit(embed=discord.Embed(color=0xef0027, description=f"{i_storeError} Você já tem este **papel de parede**."))
                if not self.user.get_money_hand(ctx.guild.id, ctx.author.id) >= 15000:
                    return await message.edit(embed=discord.Embed(color=0xef0027, description=f"{i_storeError} Dinheiro insuficiente para comprar este papel de parede."))

                self.user.post_money_hand(ctx.guild.id, ctx.author.id, -15000)
                self.user.post_inventory_background(ctx.guild.id, ctx.author.id, "Background 5")
                return await ctx.send(embed=discord.Embed(color=0x00ef5b, description=f"{i_store} Compra efetuada com sucesso!"), delete_after=300.0)

            elif message_author.content == "978":
                if "Background 6" in self.user.get_inventory_background(ctx.guild.id, ctx.author.id):
                    return await message.edit(embed=discord.Embed(color=0xef0027, description=f"{i_storeError} Você já tem este **papel de parede**."))
                if not self.user.get_money_hand(ctx.guild.id, ctx.author.id) >= 16000:
                    return await message.edit(embed=discord.Embed(color=0xef0027, description=f"{i_storeError} Dinheiro insuficiente para comprar este papel de parede."))

                self.user.post_money_hand(ctx.guild.id, ctx.author.id, -16000)
                self.user.post_inventory_background(ctx.guild.id, ctx.author.id, "Background 6")
                return await ctx.send(embed=discord.Embed(color=0x00ef5b, description=f"{i_store} Compra efetuada com sucesso!"), delete_after=300.0)

            elif message_author.content == "279":
                if "GLOCK" in self.user.get_inventory_weapon(ctx.guild.id, ctx.author.id):
                    return await message.edit(embed=discord.Embed(color=0xef0027, description=f"{i_gunStoreError} Está arma você já possui."))
                if not self.user.get_money_hand(ctx.guild.id, ctx.author.id) >= 60000:
                    return await message.edit(embed=discord.Embed(color=0xef0027, description=f"{i_gunStoreError} Dinheiro insuficiente para comprar está arma."))
                
                self.user.post_money_hand(ctx.guild.id, ctx.author.id, -60000)
                self.user.post_inventory_weapon(ctx.guild.id, ctx.author.id, "GLOCK")
                return await ctx.send(embed=discord.Embed(color=0x00ef5b, description=f"{i_gunStore} Compra efetuada com sucesso!"), delete_after=300.0)
            
            elif message_author.content == "191":
                if "M1911" in self.user.get_inventory_weapon(ctx.guild.id, ctx.author.id):
                    return await message.edit(embed=discord.Embed(color=0xef0027, description=f"{i_gunStoreError} Está arma você já possui."))
                if not self.user.get_money_hand(ctx.guild.id, ctx.author.id) >= 70000:
                    return await message.edit(embed=discord.Embed(color=0xef0027, description=f"{i_gunStoreError} Dinheiro insuficiente para comprar está arma."))
                
                self.user.post_money_hand(ctx.guild.id, ctx.author.id, -70000)
                self.user.post_inventory_weapon(ctx.guild.id, ctx.author.id, "M1911")
                return await ctx.send(embed=discord.Embed(color=0x00ef5b, description=f"{i_gunStore} Compra efetuada com sucesso!"), delete_after=300.0)

            elif message_author.content == "762":
                if "AK47" in self.user.get_inventory_weapon(ctx.guild.id, ctx.author.id):
                    return await message.edit(embed=discord.Embed(color=0xef0027, description=f"{i_gunStoreError} Está arma você já possui."))
                if not self.user.get_money_hand(ctx.guild.id, ctx.author.id) >= 110000:
                    return await message.edit(embed=discord.Embed(color=0xef0027, description=f"{i_gunStoreError} Dinheiro insuficiente para comprar está arma."))
                
                self.user.post_money_hand(ctx.guild.id, ctx.author.id, -110000)
                self.user.post_inventory_weapon(ctx.guild.id, ctx.author.id, "AK47")
                return await ctx.send(embed=discord.Embed(color=0x00ef5b, description=f"{i_gunStore} Compra efetuada com sucesso!"), delete_after=300.0)

            elif message_author.content == "556":
                if "M4A1" in self.user.get_inventory_weapon(ctx.guild.id, ctx.author.id):
                    return await message.edit(embed=discord.Embed(color=0xef0027, description=f"{i_gunStoreError} Está arma você já possui."), delete_after=300.0)
                if not self.user.get_money_hand(ctx.guild.id, ctx.author.id) >= 115000:
                    return await message.edit(embed=discord.Embed(color=0xef0027, description=f"{i_gunStoreError} Dinheiro insuficiente para comprar está arma."), delete_after=300.0)
                
                self.user.post_money_hand(ctx.guild.id, ctx.author.id, -115000)
                self.user.post_inventory_weapon(ctx.guild.id, ctx.author.id, "M4A1")
                return await ctx.send(embed=discord.Embed(color=0x00ef5b, description=f"{i_gunStore} Compra efetuada com sucesso!"), delete_after=300.0)

            else:
                return await message.edit(embed=discord.Embed(color=0xef0027, description=f"{i_storeError} Erro: O **ID** que você informou não está atribuido a nenhum item."), delete_after=300.0)

def setup(client):
    client.add_cog(MyStore(client))
