from pathlib import Path

# 0.0.1.1
# 0.0.1-rc.1
# core.major.minor.patch-rc
__author_id__ = 228537418079404033
__version__ = '1.0.0-rc'
__author__ = "Dom-kun#0053"
__name__ = 'Template'
__contact__ = 'mandinec53@gmail.com'


ROOT_DIR = Path(__file__).parent.parent
MASTER_MIGRATION = Path.joinpath(ROOT_DIR, 'src', '_migrations', 'master')
SERVER_MIGRATION = Path.joinpath(ROOT_DIR, 'src', '_migrations', 'server')
