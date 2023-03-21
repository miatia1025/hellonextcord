## miatialib ##
import os
from funcs import set_initial_variables

lib_path = set_initial_variables()
if os.path.exists(lib_path):
    print("import set_environ() from miatialib.py")

    # for api key and etcetcetc...
    from miatialib import set_environ
    from icecream import ic
    set_environ()
else:
    print("import set_environ() from funcs.py")

    # for api key and etcetcetc...
    from funcs import set_environ
    from icecream import ic
    set_environ()

## end miatialib ##

import nextcord
from nextcord.ext import commands
import logging
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.INFO)

TESTING_GUILD_ID = int(os.environ["GUILD_ID"])  # Replace with your guild ID

bot = commands.Bot()
sleeping = ThreadPoolExecutor(max_workers=2)

# event handlers
@bot.event
async def on_ready():
    channel = bot.get_channel(int(os.environ["CHANNEL_ID"]))
    await channel.send(f"{bot.user.name} is starting ...")

@bot.slash_command(description="My first slash command", guild_ids=[TESTING_GUILD_ID])
async def hello(interaction: nextcord.Interaction):
    await interaction.send("Hello!")

@bot.slash_command(description="Make miatiabot sleep")
async def logout_miatiabot(interaction: nextcord.Interaction):
    await interaction.send(f"{bot.user.name} is going to sleep ... :zzz:")
    await bot.close()


ic(TESTING_GUILD_ID)
ic(os.environ["BOT_TOKEN"])

bot.run(os.environ["BOT_TOKEN"])