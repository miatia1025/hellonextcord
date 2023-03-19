## miatialib ##
import os
from funcs import set_initial_variables

lib_path = set_initial_variables()
if 1==0:#os.path.exists(lib_path):
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

TESTING_GUILD_ID = int(os.environ["GUILD_ID"])  # Replace with your guild ID

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(description="My first slash command", guild_ids=[TESTING_GUILD_ID])
async def hello(interaction: nextcord.Interaction):
    await interaction.send("Hello!")

ic(TESTING_GUILD_ID)
ic(os.environ["BOT_TOKEN"])

bot.run(os.environ["BOT_TOKEN"])