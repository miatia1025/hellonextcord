## User Inputs

# discord bot applcation token
bot_token = ""

# your server
guild_id = ""

channel_id = ""

## End of User INputs

import os

def set_environ():
    os.environ["BOT_TOKEN"] = bot_token if bot_token else os.environ["BOT_TOKEN"]
    os.environ["GUILD_ID"] = guild_id if guild_id else os.environ["GUILD_ID"]
    os.environ["CHANNEL_ID"] = channel_id if channel_id else os.environ["CHANNEL_ID"]
    

    return 0

def set_initial_variables():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path_miatialib = os.path.join(current_dir, "miatialib.py")

    return path_miatialib