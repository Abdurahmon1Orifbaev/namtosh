from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
import os

GROUP_CHAT_ID = int(os.getenv('GROUP_CHAT_ID', '-1002457389396'))  # Fallback ID as an example
