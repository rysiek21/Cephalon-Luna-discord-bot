import discord
import json
import time
import requests

from discord.ext import commands

@commands.command()
async def sortie(ctx):
  response = requests.get('https://api.warframestat.us/pc/sortie')
  data = response.json()
  useTime = time.strftime("%H:%M", time.localtime())
  embed=discord.Embed(title="Sortie", color=0x1092c9)
  i = 0
  for variants in data["variants"]:
    i = i + 1
    embed.add_field(name=f'Mission {i}', value=f'Planet: {variants["node"]} \n Mission type: {variants["missionType"]}', inline=False)
  embed.set_footer(text=f'{useTime} • Requested by {ctx.author}')
  await ctx.send(embed=embed)

def setup(bot):
    bot.add_command(sortie)