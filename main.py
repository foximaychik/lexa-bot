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

@bot.event
async def on_guild_join(guild):
    # Attempt to send the welcome message to the first text channel
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            embed = disnake.Embed(title=f"Hello, {guild.name}!", description=f"I'm a Lexa Bot!\n My author: @foximay",
                                  color=0x701043)
            await channel.send(embed=embed)
            break

for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

bot.run(settings.TOKEN)