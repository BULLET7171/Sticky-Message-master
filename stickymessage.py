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
            if message.channel.id == 882257233872814133:
                embed = discord.Embed()
                
                embed.set_footer(text="𝙊𝙣𝙡𝙮 𝙪𝙥𝙡𝙤𝙖𝙙 𝙢𝙚𝙙𝙞𝙖 𝙝𝙚𝙧𝙚 𝙤𝙩𝙝𝙚𝙧𝙬𝙞𝙨𝙚 𝙮𝙤𝙪𝙧 𝙢𝙚𝙨𝙨𝙖𝙜𝙚 𝙬𝙞𝙡𝙡 𝙗𝙚 𝙙𝙚𝙡𝙚𝙩𝙚𝙙")
                mes = await message.channel.send(embed=embed)
                ded.clear()
                ded.append(mes)
                
        except Exception:
            print(Exception)

client.run("token")
