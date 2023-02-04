import discord
import requests
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
client = commands.Bot(command_prefix='?', intents=intents)
intents.message_content = True

TOKEN = ''

# sets the amount of minutes per check
interval = 1

# coingecko link of the desired coin. 
coin = ''

@client.event
  async def on_ready():
    print("ONLINE!!!")
    response = requests.get(coin)
    data = response.json()
    
    
@client.command()
async def servers(ctx):
    await ctx.send(f"Servers: {len(client.guilds)}")




client.run(TOKEN)
