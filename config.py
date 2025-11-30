# loanersys/config.py
import os

# Define shared network path (modify according to your network setup)
if os.name == 'nt':  # Windows
    SHARED_PATH = r'\\server\shared\loanersys'  # Network share path
else:  # Linux/Mac
    SHARED_PATH = '/mnt/shared/loanersys'  # Network mount point

# Default inventory file path
DEFAULT_INVENTORY = os.path.join(SHARED_PATH, 'loaner_inventory.csv')

# Logging file path
LOG_FILE = os.path.join(SHARED_PATH, 'loaner_system.log')
