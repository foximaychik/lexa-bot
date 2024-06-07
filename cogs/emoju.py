import disnake
from disnake.ext import commands

class Emoju(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="emoju", description="Adds ¯\\_(ツ)_/¯ to the end of your message")
    async def emoju(self, ctx, msg: str):
        await ctx.response.send_message(f"{msg} ¯\\_(ツ)_/¯")

def setup(bot):
    bot.add_cog(Emoju(bot))