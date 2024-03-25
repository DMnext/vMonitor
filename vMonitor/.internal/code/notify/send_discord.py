import discord
import time
from queue import Queue
# from discord.ext import commands
# import asyncio

# Your Discord bot token (replace 'YOUR_TOKEN' with your actual token)
TOKEN = 'MTIwOTg0MjYyMjg4NjE4NzA0OA.GcIR4r._cKb7ZsK5ijN-R_qVed0MaWnUZBL6DPIjMfshg'

message_content = "vmonitor.error : NoMessageGivenError"

# Channel ID where you want to send the message
CHANNEL_ID = 1209851503616073749
_CHANNEL_ID = 1212024170016415744

# https://discord.gg/PTGXN7Cscy
# https://poop.big-poop.de/pooping.html

# Define intents
intents = discord.Intents.default()

# Create a Discord client
client = discord.Client(intents=intents)


# Create a bot instance
# bot = commands.Bot(command_prefix='!', intents=intents)


# Command to stop the bot
# @bot.command()
# async def stop():
#     send("Stopping bot...")
#     await bot.close()
#     end_proses()


@client.event
async def on_ready():
    print(f"[INFO {time.strftime('%y.%m.%d_%H:%M:%S')}] [DISCORD] Logged in as '{client.user.name}'")
    print(f"[INFO {time.strftime('%y.%m.%d_%H:%M:%S')}] [DISCORD] Bot ID: '{client.user.id}'")

    # Find the channel by ID
    channel = client.get_channel(CHANNEL_ID)
    # Send the message
    await channel.send(message_content)
    print(f"[INFO {time.strftime('%y.%m.%d_%H:%M:%S')}] [DISCORD] Message sent: '{message_content}'")


def run():
    # Message content
    # Run the bot
    client.run(TOKEN)


def send(tasks: Queue, /):
    global message_content
    global _CHANNEL_ID
    global CHANNEL_ID

    while True:
        task_msg, task_main_msg, task_only_log = tasks.get()

        if task_msg and task_main_msg and task_only_log is None:
            exit(0)
        
        message_content = task_msg

        if task_only_log:
            CHANNEL_ID = _CHANNEL_ID
            
            client.run(TOKEN)  # running bot

        else:
            message_content = task_main_msg
            
            client.run(TOKEN)  # running bot
            
            message_content = task_msg
            CHANNEL_ID = _CHANNEL_ID
            
            client.run(TOKEN)  # running bot
            
        CHANNEL_ID = 1209851503616073749
        _CHANNEL_ID = 1212024170016415744
        # return True


"""
import discord
import asyncio

client = discord.Client()


async def my_background_task(message: str):
    await client.wait_until_ready()
    counter = 0
    channel = client.get_channel(id=1209851503616073749)  # replace with channel_id
    while not client.is_closed():
        counter += 1
        await channel.send(message)
        await asyncio.sleep(60)  # task runs every 60 seconds


@client.event
async def on_ready():
    return client.user.name, client.user.id


def send(message):
    client.loop.create_task(my_background_task(message))
    client.run('token')

"""
