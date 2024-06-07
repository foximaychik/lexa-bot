import disnake
from disnake.ext import commands
import string
import random

symbols = list(string.ascii_letters + string.digits)

class Passwordgen(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="passwordgen", description="Generates passwords")
    async def passwordgen(self, ctx, line: int):
        random.shuffle(symbols)
        out = ''.join(symbols[:line])
        embed = disnake.Embed(title="Your Password", description=f"{out}",
                              color=0x701043)
        await ctx.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Passwordgen(bot))