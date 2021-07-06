import discord
import asyncio
from gtts import gTTS
from discord.ext import commands
from discord import FFmpegPCMAudio

intents = discord.Intents.default()

intents.members = True

client = commands.Bot(command_prefix="!", intents=intents)


async def on_ready():
    print("The bot is now ready for use!")
    print("-----------------------------")


@client.command(aliases = ["911"])  # notice the brackets
async def emergency(ctx):
    channel = ctx.guild.get_channel(828004847574843482)
    voice = await channel.connect()

    def convert_to_audio(text):
        my_audio = gTTS(text)
        my_audio.save('hello.mp3')

    convert_to_audio(f"Incoming call from {ctx.author.display_name} saying {ctx.message.content}")

    def my_after(finish):
        coro = voice.disconnect()
        fut = asyncio.run_coroutine_threadsafe(coro, client.loop)

    try:
        fut.result()
    except:
        # an error happened sending the message
        pass

    source = FFmpegPCMAudio("hello.mp3")
    player = voice.play(source, after=my_after)


@client.command(aliases = ["311"])
async def nonemergency(ctx):
        channel = ctx.guild.get_channel(828004847574843482)
        voice = await channel.connect()
        def convert_to_audio(text):
            my_audio = gTTS(text)
            my_audio.save('goodbye.mp3')

        convert_to_audio(f"Incoming NON-EMERGENCY call from {ctx.author.display_name} saying {ctx.message.content}")

        def my_other_after(finish):
            coro = voice.disconnect()
            fut = asyncio.run_coroutine_threadsafe(coro, client.loop)

        try:
            fut.result()
        except:
            # an error happened sending the message
            pass

        source = FFmpegPCMAudio("goodbye.mp3")
        player = voice.play(source, after=my_other_after)


client.run("Nzg2ODEzODY3MTA3ODExMzI4.X9L3hA.o-h2frdOvSXLjUlylepBhfBBgLE")
