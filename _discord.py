import discord
import asyncio

# Your Discord bot token (replace 'YOUR_TOKEN' with your actual token)
TOKEN = 'MTIwOTg0MjYyMjg4NjE4NzA0OA.GcIR4r._cKb7ZsK5ijN-R_qVed0MaWnUZBL6DPIjMfshg'

# Channel ID where you want to send the message
CHANNEL_ID = 1209851503616073749

# https://discord.gg/PTGXN7Cscy

# Define intents
intents = discord.Intents.default()

# Create a Discord client
client = discord.Client(intents=intents)

message_content = ""


@client.event
async def on_ready():
    # print('Logged in as', client.user.name)
    # print('Bot ID:', client.user.id)

    # Find the channel by ID
    channel = client.get_channel(CHANNEL_ID)

    # Send the message
    await channel.send(message_content)
    # print('Message sent:', message_content)


def run(msg):
    # Message content
    # Run the bot
    client.run(TOKEN)
    return True


def send(message: str):
    global message_content
    message_content = message

    run(msg=message)


if __name__ == '__main__':
    from main import main
    main()


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