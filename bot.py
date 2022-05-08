import os

import interactions
import src.pm_core.config.conf as _c  # core config

from dotenv import load_dotenv


load_dotenv(".env")
bot = interactions.Client(token=os.getenv("TOKEN_DEV"),
                          intents=interactions.Intents.ALL,
                          disable_sync=_c.disable_sync) ## todo metoda

# import pm-core cogs
for filename in os.listdir("./src/pm_core/src/cogs"):
    if filename.endswith(".py"):
        bot.load(f"src.pm_core.src.cogs.{filename[:-3]}")

# import pm- sandbox cogs
for filename in os.listdir("./src/cogs"):
    if filename.endswith(".py"):
        bot.load(f"src.cogs.{filename[:-3]}")



bot.start()
