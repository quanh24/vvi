import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import chalk

Client = discord.Client()
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
                         print("san sang")
                       
@client.event
async def on_message(message):
    if message.content.upper().startswith('HELLO'):
        await client.send_message(message.channel, "Xin Chao")
     


        

client.run("NDkzNjY5OTU5MTgwODc3ODM2.Dps8lg.odn7bG3zR-IoTavM3dN1DEcfYtY")
