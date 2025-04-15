import discord
from discord import app_commands
import requests
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    print(f'Bot ready: {client.user}')

@tree.command(name="print", description="Send to Roblox")
async def print_cmd(interaction, message: str):
    try:
        url = os.getenv('FLASK_URL', 'http://localhost:5000') + "/print"
        requests.post(url, json={"message": message})
        await interaction.response.send_message(f"✅ Sent: {message}")
    except:
        await interaction.response.send_message("❌ Server offline")

client.run(os.getenv('DISCORD_TOKEN'))
