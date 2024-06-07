import disnake
from disnake.ext import commands
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import re

CLIENT_ID = 'f426c831560e4973ba462d5d17cf6795'
CLIENT_SECRET = 'f35b145feb5d485f9f36f7b193b2d461'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

class Songs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="songinfo", description="Get Spotify song information from a link")
    async def songinfo(self, inter: disnake.ApplicationCommandInteraction, link: str):
        # Extract the song ID from the URL
        match = re.match(r'https://open\.spotify\.com/track/([a-zA-Z0-9]+)', link)
        if not match:
            await inter.response.send_message("Invalid Spotify song link.")
            return

        song_id = match.group(1)
        try:
            song = sp.track(song_id)
            artists = ', '.join(artist['name'] for artist in song['artists'])
            song_info = (f"**{song['name']}** by **{artists}**\n"
                         f"Album: **{song['album']['name']}**\n"
                         f"Release Date: **{song['album']['release_date']}**\n"
                         f"Preview: [Click here]({song['preview_url']})" if song['preview_url'] else "Preview not available")
            await inter.response.send_message(song_info)
        except spotipy.exceptions.SpotifyException as e:
            await inter.response.send_message(f"An error occurred: {str(e)}")

def setup(bot):
    bot.add_cog(Songs(bot))