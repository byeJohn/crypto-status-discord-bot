import discord
import requests
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
client = commands.Bot(command_prefix='?', intents=intents)
intents.message_content = True

# User's Discord TOKEN.
TOKEN = ''

# desired crypto currency and display currency. example: 
# crypto = 'bitcoin' , currency = 'usd'
crypto = '' 
currency = ''

# sets the amount of minutes per check
interval = 1

# coingecko link of the desired coin. 
coin = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={currency}"

@client.event
  async def on_ready():
    print("ONLINE!!!")
    response = requests.get(coin)
    data = response.json()
    price = data[crypto][currency]
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"${price}"))
    client.loop.create_task(update_status())
    
# ?servers / shows the number of servers the bot is in    
@client.command()
async def servers(ctx):
    await ctx.send(f"Servers: {len(client.guilds)}")
    
# ?price / displays the price 
@client.command()
async def price(ctx):
    response = requests.get(coin)
    data = response.json()
    price = data[crypto][currency]
    await ctx.send(f"Price: ${price}")

async def update_status():
    await client.wait_until_ready()
    while not client.is_closed():
        response = requests.get(coin)
        data = response.json()
        price = data[crypto][currency]
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"${price}"))
        await asyncio.sleep(interval * 60) # pauses the program for the desired interval(minutes)

client.run(TOKEN)
