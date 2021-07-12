import discord
import time
import os

from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

@commands.command()
async def ban(ctx, member:discord.Member, reason="Nie podano"):
  if ctx.author.guild_permissions.ban_members:
    useTime = time.strftime("%H:%M", time.localtime())
    embed=discord.Embed(title='Ban', description=f'Użytkownik {member.mention} został zbanowany \n Powód: {reason}', color=0x1092c9)
    embed.set_footer(text=f'{useTime} • Requested by {ctx.author}')
    await ctx.send(embed=embed)
    embed=discord.Embed(title='Zostałeś Zbanowany', description=f'Banujacy: {ctx.author.mention} \n Powód: {reason}')
    channel = await member.create_dm()
    await channel.send(embed=embed)
    await member.ban(reason=reason)
  else:
    useTime = time.strftime("%H:%M", time.localtime())
    embed=discord.Embed(title='Ban', description='Nie posiadasz uprawnień do banowania osób', color=0x1092c9)
    embed.set_footer(text=f'{useTime} • Requested by {ctx.author}')
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_command(ban)

@ban.error
async def ban_error(ctx, error):
  if isinstance(error, commands.BadArgument):
    useTime = time.strftime("%H:%M", time.localtime())
    embed=discord.Embed(title='Ban Error', description='Podaj właściwego użytkownika', color=0x1092c9)
    embed.set_footer(text=f'{useTime} • Requested by {ctx.author}')
    await ctx.send(embed=embed)