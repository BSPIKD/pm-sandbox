import os

import interactions
import src.utils.helper as h
import pm_core.config.conf as _c  # core config
import pm_core.src.services.migration as _mg

from termcolor import cprint
from dotenv import load_dotenv

from pm_core.src.services.logs import Log

load_dotenv(".env")
bot = interactions.Client(token=os.getenv("TOKEN_DEV"),
                          intents=interactions.Intents.ALL,
                          disable_sync=_c.disable_sync)  # Todo: metoda

# import pm-core cogs
for filename in os.listdir("./pm_core/src/cogs"):
    if filename.endswith(".py"):
        bot.load(f"pm_core.src.cogs.{filename[:-3]}")

# import pm- sandbox cogs
for filename in os.listdir("./src/cogs"):
    if filename.endswith(".py"):
        bot.load(f"src.cogs.{filename[:-3]}")


@bot.event
async def on_guild_create(guild: interactions.Guild):
    """
    Event vykonaný při přidání bota na server, provede se i když se bot zapíná
    :param guild: Discord server
    """
    cprint('==========================================================================', 'cyan')
    _mg.apply_server_migrations(int(guild.id), guild.name)  # Todo: SERVER MIGRACE
    print(f"on_guild_create - {guild.name}")
    log = Log(int(guild.id))
    log.info(f'Create new guild id: {guild.id}, name: {guild.name}')


@bot.event
async def on_ready():
    """
    Event vykonaný při zapnutí
    """
    h.print_info()
    cprint('===============================================================================', 'magenta')
    _mg.apply_master_migrations()
    print("on_ready")


bot.start()
