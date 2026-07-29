import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!hello"):
        await message.channel.send("Hello there! I am awake!")

client.run("MTUzMjE1Mjg1Nzc3ODk3ODg4Ng.GlZxay.gc6EnM71jd0MskoP6RGXRPGilm5zKWMW5l_8VY")
