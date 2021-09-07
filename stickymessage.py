import discord
from discord.ext import commands
import random


intents = discord.Intents(messages=True, guilds=True, members=True)


client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("up")


storedmessage = []
@client.event
async def on_message(message):
    if message.author.bot:
        return
    for i in storedmessage:
        await i.delete()
    else:
        try:
            if message.channel.id == 882257233872814133: # channel id where the message should be sent( once the bot is online send a message in that channel and it'll start)
                embed = discord.Embed()
                
                embed.set_footer(text="Insert Text Here!")
                mes = await message.channel.send(embed=embed)
                ded.clear()
                ded.append(mes)
                
        except Exception:
            print(Exception)

client.run("token")
