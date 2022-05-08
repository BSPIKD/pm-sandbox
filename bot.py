import os

import interactions
from pyfiglet import figlet_format
from termcolor import cprint

import src.utils.helper as h
import src.pm_core.src.services.migration as _mg
import src.pm_core.config.conf as _c  # core config
import src.pm_core.src.utils.helper as _h

from dotenv import load_dotenv

load_dotenv(".env")
bot = interactions.Client(token=os.getenv("TOKEN_DEV"),
                          intents=interactions.Intents.ALL,
                          disable_sync=_c.disable_sync)  # Todo: metoda

# import pm-core cogs
for filename in os.listdir("./src/pm_core/src/cogs"):
    if filename.endswith(".py"):
        bot.load(f"src.pm_core.src.cogs.{filename[:-3]}")

# import pm- sandbox cogs
for filename in os.listdir("./src/cogs"):
    if filename.endswith(".py"):
        bot.load(f"src.cogs.{filename[:-3]}")


@bot.event
async def on_ready():
    """
    Event vykonaný při zapnutí
    """
    h.print_info()
    cprint('===============================================================================', 'magenta')
    cprint(figlet_format('MASTER  MIGRATION', font='small'), 'magenta')
    _mg.apply_master_migrations()
    print("on_ready")

bot.start()
