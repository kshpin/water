from dotenv import load_dotenv
from os import getenv

from discord.ext import commands

load_dotenv()
token = getenv("TOKEN")

bot = commands.Bot(command_prefix="&")

@bot.command(name="ping")
async def ping(ctx: commands.Context):
    await ctx.send("pong")

bot.run(token)
