import disnake
from disnake.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ping", description="Bot latency")
    async def ping(self, ctx):
        embed = disnake.Embed(title="Pong!", description=f"Bot latency is **{round(self.bot.latency * 1000)} MS**", color=0x701043)
        await ctx.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Ping(bot))