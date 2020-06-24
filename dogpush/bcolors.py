"""Constants for colorful console output."""

import sys

if sys.stdout.isatty():
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'

    ENDC = '\033[0m'
    BOLD = '\033[1m'
else:
    RED = ''
    GREEN = ''
    YELLOW = ''

    ENDC = ''
    BOLD = ''

FAIL = RED
WARNING = YELLOW
OK = GREEN
