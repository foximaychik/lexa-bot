import disnake
from disnake.ext import commands

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="avatar", description="Shows member's avatar")
    async def avatar(self, ctx, member: disnake.Member = None):
        member = member or ctx.author
        embed = disnake.Embed(title=f"{member}'s avatar", color=0x701043)
        embed.set_image(url=member.display_avatar.url)
        await ctx.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Avatar(bot))