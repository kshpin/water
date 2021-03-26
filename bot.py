"""
Authorizes and launches the bot.
Use this link to add the bot to a server:
https://discord.com/api/oauth2/authorize?client_id=824762203809775660&permissions=124992&scope=bot
"""

from os import getenv
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
token = getenv("TOKEN")

bot = commands.Bot(command_prefix="\\ ")
bot.load_extension("commands")
bot.run(token)
