import config.conf as c
import src.pm_core.config.conf as _c

from termcolor import cprint
from pyfiglet import figlet_format

"""Helper metoda specifickou aplikaci"""


def print_info():
    # PROSÍM NEMAZAT PODPIS APLIKACE
    cprint(figlet_format('Author', font='larry3d'), 'cyan')
    cprint(figlet_format(c.__author__, font='standard'), 'red')
    cprint(figlet_format(f'{c.__name__} v{c.__version__}', font='standard'), 'red')
    cprint(figlet_format(f'{_c.__name__} v{_c.__version__}', font='standard'), 'red')
    cprint(figlet_format('--------', font='larry3d'), 'blue')
    cprint(figlet_format('BOT IS READY!', font='standard'), 'blue')

