import discord
import json
import time

from discord.ext import commands

with open('./warframe-data.json', encoding='utf-8') as x:
  data = json.load(x)

@commands.command()
async def warframe(ctx, arg):
  arg = arg.lower()
  useTime = time.strftime("%H:%M", time.localtime())
  for frame in data[arg]:
    embed=discord.Embed(title=arg.capitalize(), description=frame['description'], color=0x1092c9)
    embed.add_field(name="Drop", value=frame['drop'], inline=False)
    embed.set_thumbnail(url=frame['image'])
    embed.set_footer(text=f'{useTime} • Requested by {ctx.author}')
    await ctx.send(embed=embed)

def setup(bot):
    bot.add_command(warframe)