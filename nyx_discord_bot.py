import os
import random
import asyncio
import discord
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents(messages=True, guilds=True, members=True, voice_states=True)
bot = commands.Bot(command_prefix='!', intents=intents)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():
	print(f'{bot.user} has connected to Discord!')

@bot.command()
async def start_valheim_server(ctx):
    if ctx.channel.name == "protected-propaganda-paradise":
        os.system("sudo /home/riddle/valheim_discord_bot/start_valheim.sh")
        await ctx.channel.send("Starting Valheim Server.")
    else:
        await ctx.channel.send("Server cannot be started from this channel.")

@bot.command()
async def stop_valheim_server(ctx):
    if ctx.channel.name == "protected-propaganda-paradise":
        os.system("sudo /home/riddle/valheim_discord_bot/stop_valheim.sh")
        await ctx.channel.send("Stopping Valheim Server.")
    else:
        await ctx.channel.send("Server cannot be stopped from this channel.")

@bot.command()
async def nyxnyxnyx(ctx):
    voice = ctx.author.voice
    
    if voice != None:
        voice_client = await voice.channel.connect()
        
        mp3_list = ["nyx_1.mp3", "nyx_2.mp3"]
        mp3_index = random.randint(0, 1)
        
        audio_source = discord.FFmpegPCMAudio(mp3_list[mp3_index])
        voice_client.play(audio_source)
        
        while voice_client.is_playing():
            await asyncio.sleep(1)
        else:
            await voice_client.disconnect()
            
    else:
        await ctx.channel.send("You must be in a voice channel to use this command.")
        
bot.run(TOKEN)




















