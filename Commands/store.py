from Commands.Utils.icons import getIcon
from discord.ext import commands
from Database import *

import discord

GunStoreI      = getIcon("Weapons Store")
GunStoreErrorI = getIcon("Weapons Store Error")
StoreI         = getIcon("Store")
StoreErrorI    = getIcon("Store Error")
WallpaperI     = getIcon("Image")
WalletI        = getIcon("Wallet")
BackI          = getIcon("Back")
CloseI         = getIcon("Close")
M1911Ic        = getIcon("M1911")
M4Ic           = getIcon("M4A1")
GlockIc        = getIcon("GLOCK")
AK47Ic         = getIcon("AK47")

class MyStore(commands.Cog, name="Loja"):
    def __init__(self, bot):
        self.client = bot
        self.check  = database.check()
        self.guild  = database.guild()
        self.user   = database.user()

    @commands.command(aliases=['store'])
    @commands.guild_only()
    async def loja(self, ctx):
        messageStore = await ctx.send(embed=discord.Embed(title=f"{StoreI} Store - {ctx.guild.name}", color=0x6600db, description=f"""
    ``Papel de parede ​:`` {WallpaperI}
    ``Armas​ ​​ ​​      ​​ ​​​​ ​​​ ​​:`` {GunStoreI}
    ⠀
    ``Comprar​ ​​      ​​ ​​ ​:`` {WalletI}
    ``Fechar​      ​​ ​​ ​​ ​​ ​:`` {CloseI}"""), delete_after=600.0)

        for x in [CloseI, WalletI, "➖", WallpaperI, GunStoreI]:
            await messageStore.add_reaction(x)

        def checkerReaction(reaction, user):
            return reaction.message.id == messageStore.id and user == ctx.author
        def checkerMessage(message):
            return message.author == ctx.author and message.channel == ctx.channel

        while True:
            try:
                reaction, user = await self.client.wait_for('reaction_add', check=checkerReaction, timeout=300.0)
            except:
                return messageStore.edit(embed=discord.Embed(color=0xef0027, title=f"{StoreErrorI} Seu tempo expirou."))
            
            if reaction.emoji.name == "Fechar":
                await messageStore.delete()

            if reaction.emoji.name == "image":
                embed = discord.Embed(title=f"{WallpaperI} Store - Papel de Parede", color=0x6600db)
                embed.add_field(name="Background 1", value="**ID:** 154\n**Preço:** R$10000\n**Papel de Parede:** [**Clique aqui**](https://i.imgur.com/nhEfmIY.jpg)")
                embed.add_field(name="Background 2", value="**ID:** 413\n**Preço:** R$12000\n**Papel de Parede:** [**Clique aqui**](https://i.imgur.com/UM0icxL.jpg)")
                embed.add_field(name="Background 3", value="**ID:** 456\n**Preço:** R$13000\n**Papel de Parede:** [**Clique aqui**](https://i.imgur.com/7Lg3aRy.jpg)")
                embed.add_field(name="Background 4", value="**ID:** 867\n**Preço:** R$14000\n**Papel de Parede:** [**Clique aqui**](https://i.imgur.com/M1SEbiF.jpg)")
                embed.add_field(name="Background 5", value="**ID:** 345\n**Preço:** R$15000\n**Papel de Parede:** [**Clique aqui**](https://i.imgur.com/8zNOkSC.jpg)")
                embed.add_field(name="Background 6", value="**ID:** 978\n**Preço:** R$16000\n**Papel de Parede:** [**Clique aqui**](https://i.imgur.com/2ys3opI.jpg)")
                await messageStore.edit(embed=embed)

            if reaction.emoji.name == "Loja_de_Armas":
                embed = discord.Embed(title=f"{GunStoreI} Store - Armas", color=0x6600db)
                embed.add_field(name="Glock", value=f"**ID:** 279\n**Preço:** R$60000\n**Ícone:** {GlockIc}")
                embed.add_field(name="M1911", value=f"**ID:** 191\n**Preço:** R$70000\n**Ícone:** {M1911Ic}")
                embed.add_field(name="AK-47", value=f"**ID:** 762\n**Preço:** R$110000\n**Ícone:** {AK47Ic}")
                embed.add_field(name="M4", value=f"**ID:** 556\n**Preço:** R$115000\n**Ícone:** {M4Ic}")
                await messageStore.edit(embed=embed)

            if reaction.emoji.name == "carteira":
                await messageStore.clear_reactions()
                await messageStore.edit(embed=discord.Embed(color=0x00ef5b, description=f"{WalletI} Qual o ID do item/papel de parede/arma que deseja ?"))
                #await messageStore.add_reaction(":close:621291283058524160")
                
                try:
                    message = await self.client.wait_for('message', check=checkerMessage, timeout=300.0)
                except:
                    return messageStore.edit(embed=discord.Embed(color=0xef0027, title=f"{StoreErrorI} Seu tempo expirou."))

                if int(message.content) == 154:
                    if "Background 1" in self.user.get_inventoryBackground(ctx.guild.id, ctx.author.id):
                        return await messageStore.edit(embed=discord.Embed(color=0xef0027, description=f"{StoreErrorI} Você já tem este **papel de parede**."))
                    if not self.user.get_moneyHand(ctx.guild.id, ctx.author.id) >= 10000:
                        return await messageStore.edit(embed=discord.Embed(color=0xef0027, description=f"{StoreErrorI} Dinheiro Insuficiente para comprar este papel de parede."))
                    
                    self.user.post_moneyHand(ctx.guild.id, ctx.author.id, -10000)
                    self.user.post_inventoryBackground(ctx.guild.id, ctx.author.id, "Background 1")
                    return await ctx.send(embed=discord.Embed(color=0x00ef5b, description=f"{StoreI} Compra efetuada com sucesso!"), delete_after=300.0)

                elif int(message.content) == 413:
                    if "Background 2" in self.user.get_inventoryBackground(ctx.guild.id, ctx.author.id):
                        return await messageStore.edit(embed=discord.Embed(color=0xef0027, description=f"{StoreErrorI} Você já tem este **papel de parede**."))
                    if not self.user.get_moneyHand(ctx.guild.id, ctx.author.id) >= 12000:
                        return await messageStore.edit(embed=discord.Embed(color=0xef0027, description=f"{StoreErrorI} Dinheiro Insuficiente para comprar este papel de parede."))

                    self.user.post_moneyHand(ctx.guild.id, ctx.author.id, -12000)
                    self.user.post_inventoryBackground(ctx.guild.id, ctx.author.id, "Background 2")
                    return await ctx.send(embed=discord.Embed(color=0x00ef5b, description=f"{StoreI} Compra efetuada com sucesso!"), delete_after=300.0)

                elif int(message.content) == 456:
                    if "Background 3" in self.user.get_inventoryBackground(ctx.guild.id, ctx.author.id):
                        return await messageStore.edit(embed=discord.Embed(color=0xef0027, description=f"{StoreErrorI} Você já tem este **papel de parede**."))
                    if not self.user.get_moneyHand(ctx.guild.id, ctx.author.id) >= 13000:
                        return await messageStore.edit(embed=discord.Embed(color=0xef0027, description=f"{StoreErrorI} Dinheiro Insuficiente para comprar este papel de parede."))

                    self.user.post_moneyHand(ctx.guild.id, ctx.author.id, -13000)
                    self.user.post_inventoryBackground(ctx.guild.id, ctx.author.id, "Background 3")
                    return await ctx.send(embed=discord.Embed(color=0x00ef5b, description=f"{StoreI} Compra efetuada com sucesso!"), delete_after=300.0)

                elif int(message.content) == 867:
                    if "Background 4" in self.user.get_inventoryBackground(ctx.guild.id, ctx.author.id):
                        return await messageStore.edit(embed=discord.Embed(color=0xef0027, description=f"{StoreErrorI} Você já tem este **papel de parede**."))
                    if not self.user.get_moneyHand(ctx.guild.id, ctx.author.id) >= 14000:
                        return await messageStore.edit(embed=discord.Embed(color=0xef0027, description=f"{StoreErrorI} Dinheiro Insuficiente para comprar este papel de parede."))

                    self.user.post_moneyHand(ctx.guild.id, ctx.author.id, -14000)
                    self.user.post_inventoryBackground(ctx.guild.id, ctx.author.id, "Background 4")
                    return await ctx.send(embed=discord.Embed(color=0x00ef5b, description=f"{StoreI} Compra efetuada com sucesso!"), delete_after=300.0)

                elif int(message.content) == 345:
                    if "Background 5" in self.user.get_inventoryBackground(ctx.guild.id, ctx.author.id):
                        return await messageStore.edit(embed=discord.Embed(color=0xef0027, description=f"{StoreErrorI} Você já tem este **papel de parede**."))
                    if not self.user.get_moneyHand(ctx.guild.id, ctx.author.id) >= 15000:
                        return await messageStore.edit(embed=discord.Embed(color=0xef0027, description=f"{StoreErrorI} Dinheiro Insuficiente para comprar este papel de parede."))

                    self.user.post_moneyHand(ctx.guild.id, ctx.author.id, -15000)
                    self.user.post_inventoryBackground(ctx.guild.id, ctx.author.id, "Background 5")
                    return await ctx.send(embed=discord.Embed(color=0x00ef5b, description=f"{StoreI} Compra efetuada com sucesso!"), delete_after=300.0)

                elif int(message.content) == 978:
                    if "Background 6" in self.user.get_inventoryBackground(ctx.guild.id, ctx.author.id):
                        return await messageStore.edit(embed=discord.Embed(color=0xef0027, description=f"{StoreErrorI} Você já tem este **papel de parede**."))
                    if not self.user.get_moneyHand(ctx.guild.id, ctx.author.id) >= 16000:
                        return await messageStore.edit(embed=discord.Embed(color=0xef0027, description=f"{StoreErrorI} Dinheiro Insuficiente para comprar este papel de parede."))

                    self.user.post_moneyHand(ctx.guild.id, ctx.author.id, -16000)
                    self.user.post_inventoryBackground(ctx.guild.id, ctx.author.id, "Background 6")
                    return await ctx.send(embed=discord.Embed(color=0x00ef5b, description=f"{StoreI} Compra efetuada com sucesso!"), delete_after=300.0)

                elif int(message.content) == 279:
                    if "GLOCK" in self.user.get_inventoryWeapon(ctx.guild.id, ctx.author.id):
                        return await messageStore.edit(embed=discord.Embed(color=0xef0027, description=f"{GunStoreErrorI} Está arma você já possui."))
                    if not self.user.get_moneyHand(ctx.guild.id, ctx.author.id) >= 60000:
                        return await messageStore.edit(embed=discord.Embed(color=0xef0027, description=f"{GunStoreErrorI} Dinheiro Insuficiente para comprar está arma."))
                    
                    self.user.post_moneyHand(ctx.guild.id, ctx.author.id, -60000)
                    self.user.post_inventoryWeapon(ctx.guild.id, ctx.author.id, "GLOCK")
                    return await ctx.send(embed=discord.Embed(color=0x00ef5b, description=f"{GunStoreI} Compra efetuada com sucesso!"), delete_after=300.0)
                
                elif int(message.content) == 191:
                    if "M1911" in self.user.get_inventoryWeapon(ctx.guild.id, ctx.author.id):
                        return await messageStore.edit(embed=discord.Embed(color=0xef0027, description=f"{GunStoreErrorI} Está arma você já possui."))
                    if not self.user.get_moneyHand(ctx.guild.id, ctx.author.id) >= 70000:
                        return await messageStore.edit(embed=discord.Embed(color=0xef0027, description=f"{GunStoreErrorI} Dinheiro Insuficiente para comprar está arma."))
                    
                    self.user.post_moneyHand(ctx.guild.id, ctx.author.id, -70000)
                    self.user.post_inventoryWeapon(ctx.guild.id, ctx.author.id, "M1911")
                    return await ctx.send(embed=discord.Embed(color=0x00ef5b, description=f"{GunStoreI} Compra efetuada com sucesso!"), delete_after=300.0)

                elif int(message.content) == 762:
                    if "AK47" in self.user.get_inventoryWeapon(ctx.guild.id, ctx.author.id):
                        return await messageStore.edit(embed=discord.Embed(color=0xef0027, description=f"{GunStoreErrorI} Está arma você já possui."))
                    if not self.user.get_moneyHand(ctx.guild.id, ctx.author.id) >= 110000:
                        return await messageStore.edit(embed=discord.Embed(color=0xef0027, description=f"{GunStoreErrorI} Dinheiro Insuficiente para comprar está arma."))
                    
                    self.user.post_moneyHand(ctx.guild.id, ctx.author.id, -110000)
                    self.user.post_inventoryWeapon(ctx.guild.id, ctx.author.id, "AK47")
                    return await ctx.send(embed=discord.Embed(color=0x00ef5b, description=f"{GunStoreI} Compra efetuada com sucesso!"), delete_after=300.0)

                elif int(message.content) == 556:
                    if "M4A1" in self.user.get_inventoryWeapon(ctx.guild.id, ctx.author.id):
                        return await messageStore.edit(embed=discord.Embed(color=0xef0027, description=f"{GunStoreErrorI} Está arma você já possui."))
                    if not self.user.get_moneyHand(ctx.guild.id, ctx.author.id) >= 115000:
                        return await messageStore.edit(embed=discord.Embed(color=0xef0027, description=f"{GunStoreErrorI} Dinheiro Insuficiente para comprar está arma."))
                    
                    self.user.post_moneyHand(ctx.guild.id, ctx.author.id, -115000)
                    self.user.post_inventoryWeapon(ctx.guild.id, ctx.author.id, "M4A1")
                    return await ctx.send(embed=discord.Embed(color=0x00ef5b, description=f"{GunStoreI} Compra efetuada com sucesso!"), delete_after=300.0)
                
                elif message.content in ["exit", "close", "fechar", "excluir"]:
                    await messageStore.delete()

                else:
                    return await messageStore.edit(embed=discord.Embed(color=0xef0027, description=f"{StoreErrorI} Erro: O **ID** que você informou não está atribuido a nenhum item."))
            
                #await messageStore.delete()

def setup(bot):
    bot.add_cog(MyStore(bot))
