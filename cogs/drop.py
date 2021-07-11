import discord
import json
import time

from discord.ext import commands

with open('./drop-data.json', encoding='utf-8') as x:
  data = json.load(x)

@commands.command()
async def drop(ctx, *args):
  arg = ''.join(args)
  arg = arg.lower()
  useTime = time.strftime("%H:%M", time.localtime())
  for item in data[arg]:
    embed=discord.Embed(title=item['label'], description="", color=0x1092c9)
  i = 0
  for item in data[arg]:
    embed.set_thumbnail(url=item['image'])
    for place in item["drop"]:
      i=i+1
      embed.add_field(name=f'Farm {i}', value=f"{place}", inline=False)
  embed.set_footer(text=f'{useTime} • Requested by {ctx.author}')
  await ctx.send(embed=embed)

def setup(bot):
    bot.add_command(drop)