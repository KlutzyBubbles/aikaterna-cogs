import aiohttp
import discord
from redbot.core import commands


BaseCog = getattr(commands, "Cog", object)

class Inspirobot(BaseCog):
    """Posts images generated by https://inspirobot.me"""
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()

    @commands.command()
    async def inspireme(self, ctx):
        """Fetch a random "inspirational message" from the bot."""
        try:
            async with self.session.request(
                "GET", "http://inspirobot.me/api?generate=true"
            ) as page:
                pic = await page.text(encoding="utf-8")
                em = discord.Embed()
                em.set_image(url=pic)
                await ctx.send(embed=em)
        except Exception as e:
            await ctx.send(f"Oops, there was a problem: {e}")

    def __unload(self):
        self.session.close()
