from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
GROUP_CHAT_ID = int(env.str("GROUP_CHAT_ID", "-1002457389396"))  # Default fallback

