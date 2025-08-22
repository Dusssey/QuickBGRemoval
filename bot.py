import discord
from discord.ext import commands
import requests
from io import BytesIO
import json

# Load config.json
with open("config.json") as f:
    config = json.load(f)

DISCORD_TOKEN = config["DISCORD_TOKEN"]
REMOVE_BG_API_KEY = config["REMOVE_BG_API_KEY"]

PREFIX = "!"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def removebg(ctx, url: str = None):
    """Remove background from image via attachment or URL"""
    if not url and not ctx.message.attachments:
        return await ctx.send("❌ Please attach an image or give me a URL!")

    # Get image bytes (from URL or attachment)
    if url:
        img_bytes = requests.get(url).content
    else:
        attachment = ctx.message.attachments[0]
        img_bytes = await attachment.read()

    # Send to remove.bg API
    response = requests.post(
        "https://api.remove.bg/v1.0/removebg",
        files={"image_file": img_bytes},
        data={"size": "auto"},
        headers={"X-Api-Key": REMOVE_BG_API_KEY},
    )

    # Send result
    if response.status_code == 200:
        file = discord.File(BytesIO(response.content), filename="transparent.png")
        await ctx.send(file=file)
    else:
        await ctx.send(f"❌ Failed: {response.status_code} - {response.text}")

bot.run(DISCORD_TOKEN)
