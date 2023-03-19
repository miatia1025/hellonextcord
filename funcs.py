import os

def set_environ():
    os.environ["BOT_TOKEN"] = "REPLACE THIS WITH YOUR BOT TOKEN"
    os.environ["GUILD_ID"] = "REPLACE THIS WITH YOUR SERVER ID"

    return 0

def set_initial_variables():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path_miatialib = os.path.join(current_dir, "miatialib.py")

    return path_miatialib