import discord
import json
import time
import requests

from discord.ext import commands

@commands.command()
async def invasions(ctx):
  response = requests.get('https://api.warframestat.us/pc/invasions')
  data = response.json()
  useTime = time.strftime("%H:%M", time.localtime())
  embed=discord.Embed(title="Invasions", color=0x1092c9)
  i = 0
  for invasion in data:
    i = i + 1
    if json.dumps(invasion["vsInfestation"]) == "false":
      embed.add_field(name=f'Inwazja {i}', value=f'Atakujący: {invasion["attacker"]["faction"]} \n Nagroda: {invasion["attacker"]["reward"]["asString"]} \n \n Broniący: {invasion["defender"]["faction"]} \n Nagroda: {invasion["defender"]["reward"]["asString"]}', inline=True)
    else:
      embed.add_field(name=f'Inwazja {i}', value=f'Atakujący: {invasion["attacker"]["faction"]} \n \n Broniący: {invasion["defender"]["faction"]} \n Nagroda: {invasion["defender"]["reward"]["asString"]}', inline=True)
  embed.set_footer(text=f'{useTime} • Requested by {ctx.author}')
  await ctx.send(embed=embed)

def setup(bot):
    bot.add_command(invasions)