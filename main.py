import os
import discord

from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

client = commands.Bot(command_prefix={os.getenv('PREFIX')})
key = os.getenv('TOKEN')

@client.event
async def on_ready():
  activity = discord.Activity(type=discord.ActivityType.listening, name=os.getenv('ACTIVITY'))
  await client.change_presence(activity = activity)
  print('Bot is running')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

client.run(key)