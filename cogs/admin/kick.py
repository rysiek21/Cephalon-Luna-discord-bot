import discord
import time
import os

from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

@commands.command()
async def kick(ctx, member:discord.Member, reason="Nie podano"):
  if ctx.author.guild_permissions.kick_members:
    useTime = time.strftime("%H:%M", time.localtime())
    embed=discord.Embed(title='Kick', description=f'Użytkownik {member.mention} został wyrzucony \n Powód: {reason}', color=0x1092c9)
    embed.set_footer(text=f'{useTime} • Requested by {ctx.author}')
    await ctx.send(embed=embed)
    embed=discord.Embed(title='Zostałeś Wyrzucony', description=f'Wyrzucający: {ctx.author.mention} \n Powód: {reason}')
    channel = await member.create_dm()
    await channel.send(embed=embed)
    await member.kick(reason=reason)
  else:
    useTime = time.strftime("%H:%M", time.localtime())
    embed=discord.Embed(title='Kick', description='Nie posiadasz uprawnień do wyrzucania osób', color=0x1092c9)
    embed.set_footer(text=f'{useTime} • Requested by {ctx.author}')
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_command(kick)

@kick.error
async def kick_error(ctx, error):
  if isinstance(error, commands.BadArgument):
    useTime = time.strftime("%H:%M", time.localtime())
    embed=discord.Embed(title='Kick Error', description='Podaj właściwego użytkownika', color=0x1092c9)
    embed.set_footer(text=f'{useTime} • Requested by {ctx.author}')
    await ctx.send(embed=embed)