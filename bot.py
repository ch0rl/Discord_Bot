"""Main bot file"""

import logging
logging.basicConfig(
    filename=".log",
    filemode="a",
    format="%(asctime)s : %(levelname)s : %(name)s : %(message)s"
)

import json
import discord
from typing import Dict, List
from discord.ext import commands

with open("vars.json", "r") as f:
    vars_ = json.load(f)

app_id: str = vars_["APP-ID"]
token: str = vars_["TOKEN"]

bot = commands.Bot(command_prefix="!c ", activity=discord.Game("!c help"))
bot.load_extension("cogs.general")
bot.load_extension("cogs.custom_commands")
bot.load_extension("cogs.make_quotes")
bot.run(token)
