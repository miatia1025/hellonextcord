## User Inputs

# discord bot applcation token
bot_token = ""

# your server
guild_id = ""

## End of User INputs

import os


def set_environ():
    from dotenv import load_dotenv
    load_dotenv()
    
    return 0

def set_initial_variables():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path_miatialib = os.path.join(current_dir, "miatialib.py")

    return path_miatialib