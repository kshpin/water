"""
Implements bot functionality.
"""

from pprint import pprint

import discord
from discord.ext.commands import Bot, Cog, Context, MinimalHelpCommand, command

import aiohttp

def setup(bot: Bot):
    """
    Adds the cog to the given bot.
    """

    bot.add_cog(Commands(bot))

class HelpCommand(MinimalHelpCommand):
    """
    Help command override class.
    """

    def get_command_signature(self, comm):
        """
        Returns the string describing a command.
        """

        return "{0.clean_prefix}{1.qualified_name} {1.signature}".format(self, comm)

class Commands(Cog):
    """
    The bot class, implements all its functionality.
    """

    def __init__(self, bot: Bot):
        self.bot = bot

    @command(name="ping")
    async def ping(self, ctx: Context):
        """
        Ping, returns pong and latency.
        """

        await ctx.send(f"pong\n{round(self.bot.latency * 1000)}ms")

    @command(name="setstatus")
    async def setstatus(self, ctx: Context, *, text: str):
        """
        Set the bot's status.
        """

        await self.bot.change_presence(activity=discord.Game(name=text))

    @command(name="git")
    async def git(self, ctx: Context, *, text: str):
        """
        Searches Github and returns a link to the top result
        """

        payload = {
            "per_page": "1",
            "page": "1",
            "q": text
        }

        error = False
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.github.com/search/repositories", params=payload) as resp:
                if resp.status != 200:
                    await ctx.send(f"error code: {resp.status}")
                    pprint(await resp.json())
                    error = True
                r = await resp.json()

        if not error:
            await ctx.send(r["items"][0]["html_url"])


    @command(name="shork!")
    async def shork(self, ctx: Context):
        """
        shork!
        """

        await ctx.send("krill! :shrimp:")

    @command(name="krill!")
    async def krill(self, ctx: Context):
        """
        krill!
        """

        await ctx.send("shork! :shark:")
