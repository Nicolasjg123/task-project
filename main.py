import sys
from interface import cli
from interface import rest

if len(sys.argv) < 2:
    cli.start()
else:
    interface = sys.argv[1].lower()
    if interface == "cli":
        cli.start()
    elif interface == "rest":
        rest.start()