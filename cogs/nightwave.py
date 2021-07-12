import discord
import json
import time
import requests

from discord.ext import commands

@commands.command()
async def nightwave(ctx):
  response = requests.get('https://api.warframestat.us/pc/nightwave')
  data = response.json()
  useTime = time.strftime("%H:%M", time.localtime())
  embed=discord.Embed(title=f'Nightwave {data["tag"]}  :  Sezon {data["season"]}', description=f'Koniec: {data["expiry"][:-14]}', color=0x1092c9)
  for challange in data["activeChallenges"]:
    embed.add_field(name=f'{challange["title"]}', value=f'Opis: {challange["desc"]} \n Reputacja: {challange["reputation"]}', inline=False)
  embed.set_footer(text=f'{useTime} • Requested by {ctx.author}')
  await ctx.send(embed=embed)

def setup(bot):
    bot.add_command(nightwave)