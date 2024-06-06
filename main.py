import disnake
from disnake.ext import commands
import os
import art
import settings

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    art.tprint("Activated!")


for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

bot.run(settings.TOKEN)
