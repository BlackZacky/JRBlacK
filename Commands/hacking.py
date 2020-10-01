from socket import gethostbyname
from discord.ext import commands
from datetime import datetime
from Database import *
from . import sub_commands

import discord
import whois
import nmap3

class MyHacking(commands.Cog, name="Hacking"):
    def __init__(self, client):
        self.client = client
        self.check = database.check()
        self.guild = database.guild()
        self.user  = database.user()
        self.nmap  = nmap3.Nmap()

    @commands.group(name="nmap", aliases=["nmp", "scan"], usage="[p]nmap [sub comando]")
    @commands.guild_only()
    async def _nmap(self, ctx):
        if ctx.invoked_subcommand is None:
            return await sub_commands(self.client, ctx, ctx.command.name)

    @_nmap.command(aliases=["tp"], usage="[p]nmap top_ports [ip]")
    @commands.guild_only()
    async def top_ports(self, ctx, host_ip):
        results = self.nmap.scan_top_ports(gethostbyname(host_ip))

        nmap_scan_list = []
        for x in results[gethostbyname(host_ip)]:
            nmap_scan_list.append(f"{x['portid']}  {x['protocol']}  {x['state']}  {x['service']['name']}")

        await ctx.send(embed=discord.Embed(description="**```{}```**".format("\n".join(nmap_scan_list))))

    @commands.command()
    @commands.guild_only()
    async def whois(self, ctx, domain:str):
        whois_get = whois.whois(domain)

        embed = discord.Embed(title="Whois Domain")
        
        if not "null" in whois_get.domain_name:
            embed.add_field(name="Nome do Dominio:", value=f"```{whois_get.domain_name}```")
        
        try:
            embed.add_field(name="Data de Update:", value=f"```{whois_get.updated_date[0].day}/{whois_get.updated_date[0].month}/{whois_get.updated_date[0].year}```")
        except:
            embed.add_field(name="Data de Update:", value=f"```{whois_get.updated_date.day}/{whois_get.updated_date.month}/{whois_get.updated_date.year}```")
        try:
            embed.add_field(name="Data de Criação:", value=f"```{whois_get.creation_date[0]}/{whois_get.creation_date[0].month}/{whois_get.creation_date[0].year}```")
        except:
            embed.add_field(name="Data de Criação:", value=f"```{whois_get.creation_date}/{whois_get.creation_date.month}/{whois_get.creation_date.year}```")
        try:
            embed.add_field(name="Data de Expiração:", value=f"```{whois_get.expiration_date[0]}/{whois_get.expiration_date[0].month}/{whois_get.expiration_date[0].year}```")
        except:
            embed.add_field(name="Data de Expiração:", value=f"```{whois_get.expiration_date}/{whois_get.expiration_date.month}/{whois_get.expiration_date.year}```")
        try:
            if not "null" in whois_get.emails:
                embed.add_field(name="Email:", value=f"```{whois_get.emails[0]}```")
        except:
            if not "null" in whois_get.emails:
                embed.add_field(name="Email:", value=f"```{whois_get.emails}```")
 

 
        if not "null" in whois_get.org:
            embed.add_field(name="Organização:", value=f"```{whois_get.org}```")

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(MyHacking(client))