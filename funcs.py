## User Inputs

# discord bot applcation token
bot_token = ""

# your server
guild_id = ""

## End of User INputs

import os


def set_environ():
    if bot_token or guild_id == None:
        print("read environ from funcs.py")
        os.environ["BOT_TOKEN"] = bot_token
        os.environ["GUILD_ID"] = guild_id
    else:
        print("read environ from machine")

    return 0

def set_initial_variables():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path_miatialib = os.path.join(current_dir, "miatialib.py")

    return path_miatialib