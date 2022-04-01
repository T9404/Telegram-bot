from environs import Env


env = Env()
env.read_env()


BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")


dbname = env.str('dbname')
user = env.str("user")
password = env.str("password")
host = env.str("host")
