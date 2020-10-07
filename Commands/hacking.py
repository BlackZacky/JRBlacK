from socket import gethostbyname
from discord.ext import commands
from datetime import datetime
from Database import *
from . import sub_commands

import asyncio
import discord
import whois
import nmap

class MyHacking(commands.Cog, name="Hacking"):
    def __init__(self, client):
        self.client = client
        self.nmap = nmap.PortScanner()
    
    @commands.group(name="nmap", aliases=["nmp", "scan"], usage="[p]nmap [sub comando]")
    @commands.guild_only()
    async def _nmap(self, ctx):
        if ctx.invoked_subcommand is None:
            return await sub_commands(self.client, ctx, ctx.command.name)

    @_nmap.command(aliases=["tp"], usage="[p]nmap top_ports [ip]")
    @commands.guild_only()
    async def top_ports(self, ctx, host_ip):
        get_host_ip = gethostbyname(host_ip)

        self.nmap.scan(get_host_ip)
        await asyncio.sleep(0.1)

        infos = {}
        for host in self.nmap.all_hosts():
            infos["host"] = {"ip": host, "name": self.nmap[host].hostname(), "state": self.nmap[host].state()}
            for proto in self.nmap[host].all_protocols():
                infos["protocol"] = proto
                lport = self.nmap[host][proto].keys()
                infos["ports"] = []
                for port in lport:
                    infos["ports"].append('port : %s\tstate : %s' % (port, self.nmap[host][proto][port]['state']))

        embed = discord.Embed(description="""
----------------------------------------------------
Host : %s (%s)
State : %s
----------------------------------------------------
Protocol : %s

%s

""" % (infos['host']["ip"], infos['host']['name'], infos['host']['state'], infos['protocol'], '\n'.join(infos['ports'])))

        await ctx.send(embed=embed)

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