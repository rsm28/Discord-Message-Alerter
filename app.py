import discord
from discord.utils import get
import json, os
from utils import grabRecipe, grabInstructions

if not os.path.exists("config.json"):
    print(">> config.json is missing. Please create it.")
    print(">> Exiting...")
    exit(1)

with open("config.json", "r") as f:
    config = json.load(f)
    if (
        "token" not in config
        or "user_id" not in config
        or "openai_api_key" not in config
    ):
        print(">> config.json is missing arguments. Please add them.")
        print(">> Exiting...")
        exit(1)

config = json.load(open("config.json"))
TOKEN = config["token"]
USER_ID = config["user_id"]
OAI_API_KEY = config["openai_api_key"]
USER_ID = int(USER_ID)


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    global ingredients
    if message.author == client.user:
        return

    # recipe generator
    if message.channel.id == 811687698171035759:
        if message.content.startswith("!recipe"):
            print("recipe command detected")
            channel = client.get_channel(811687698171035759)
            await channel.send(grabRecipe(message.content, OAI_API_KEY))

            ingredients = []
            for line in message.content.splitlines():
                ingredients.append(line)
            ingredients.remove("!recipe")

    # recipe instruction generator
    if message.channel.id == 811687698171035759:
        if message.content.startswith("!instructions"):
            print("instructions command detected")
            channel = client.get_channel(811687698171035759)

            # get rid of "!instructions " from the message
            prompt = message.content[14:]
            await channel.send(grabInstructions(prompt, ingredients, OAI_API_KEY))

    if message.author.id == USER_ID:
        print("Message sent by user with USER_ID")
        return

    # if any message is sent at all, send a DM to the user with USER_ID
    user = await client.fetch_user(USER_ID)
    await user.create_dm()
    # create a message with "Message Received!"
    await user.dm_channel.send(
        f"Message Received in {message.channel}, in {message.guild}. Click here to view: {message.jump_url}"
    )

    print(
        f"Message Received in {message.channel}, in {message.guild}. Click here to view: {message.jump_url}"
    )


client.run(TOKEN)
