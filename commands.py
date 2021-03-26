"""
Implements bot functionality.
"""

import discord
from discord.ext import commands

def setup(bot: commands.Bot):
    """
    Adds the cog to the given bot.
    """

    bot.add_cog(Commands(bot))

class Commands(commands.Cog):
    """
    The bot class, implements all its functionality.
    """

    def __init__(self, b: commands.Bot):
        self.bot = b

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        """
        Ping, returns pong and latency.
        """

        await ctx.send(f"pong\n{round(self.bot.latency * 1000)}ms")

    @commands.command(name="setstatus")
    async def setstatus(self, ctx: commands.Context, *, text: str):
        """
        Set the bot's status.
        """
        await self.bot.change_presence(activity=discord.Game(name=text))

    @commands.command(name="shork!")
    async def shork(self, ctx: commands.Context):
        """
        shork!
        """

        await ctx.send("krill! :shrimp:")

    @commands.command(name="krill!")
    async def krill(self, ctx: commands.Context):
        """
        krill!
        """

        await ctx.send("shork! :shark:")
