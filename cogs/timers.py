import discord
import json
import time
import requests

from discord.ext import commands

@commands.command()
async def timers(ctx):
  responseCetsus = requests.get('https://api.warframestat.us/pc/cetusCycle')
  dataCetus = responseCetsus.json()
  responseVallis = requests.get('https://api.warframestat.us/pc/vallisCycle')
  dataVallis = responseVallis.json()
  responseEarth = requests.get('https://api.warframestat.us/pc/earthCycle')
  dataEarth = responseEarth.json()
  useTime = time.strftime("%H:%M", time.localtime())
  embed=discord.Embed(title="Timers", color=0x1092c9)
  embed.add_field(name='Cetus Timer', value=f"Cykl: {dataCetus['state'].capitalize()} \n Pozostały czas: {dataCetus['timeLeft']}", inline=False)
  embed.add_field(name='Orb Vallis Timer', value=f"Cykl: {dataVallis['state'].capitalize()} \n Pozostały czas: {dataVallis['timeLeft']}", inline=False)
  embed.add_field(name='Earth Timer', value=f"Cykl: {dataEarth['state'].capitalize()} \n Pozostały czas: {dataEarth['timeLeft']}", inline=False)
  embed.set_footer(text=f'{useTime} • Requested by {ctx.author}')
  await ctx.send(embed=embed)

def setup(bot):
    bot.add_command(timers)