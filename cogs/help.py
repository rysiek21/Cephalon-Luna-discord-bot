import discord
import time
import os

from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

@commands.command()
async def help(ctx):
  useTime = time.strftime("%H:%M", time.localtime())
  embed=discord.Embed(title="Help", color=0x1092c9)
  embed.add_field(name=f"{os.getenv('PREFIX')}Drop [surowiec]", value='Pokazuje drop wybranego surowca', inline=False)
  embed.add_field(name=f"{os.getenv('PREFIX')}Warframe [warframe]", value='Pokazuje drop wybranego Warframe', inline=False)
  embed.add_field(name=f"{os.getenv('PREFIX')}Invasions", value='Pokazuje aktywne inwazje', inline=False)
  embed.add_field(name=f"{os.getenv('PREFIX')}Sortie", value='Pokazuje aktywne sortie', inline=False)
  embed.add_field(name=f"{os.getenv('PREFIX')}Timers", value='Pokazuje cykl świata', inline=False)
  embed.set_footer(text=f'{useTime} • Requested by {ctx.author}')
  await ctx.send(embed=embed)

def setup(bot):
  bot.remove_command('help')
  bot.add_command(help)