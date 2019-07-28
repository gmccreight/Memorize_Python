#!/usr/bin/env python3

# This is the script for working with this project.  It will grow over time.

# Symlink this file into a place in your path for easy commands.

# In your bash aliases, you should consider doing something like this:

# function mp {
#   if [ "$1" = "cd" ]; then
#     cd ~/Memorize_Python
#     return
#   fi
#
#   # if you like Vim
#   if [ "$1" = "e" ]; then
#     cd ~/Memorize_Python
#     mvim -c "Mp"
#     return
#   fi
#
#   (
#     cd ~/Memorize_Python
#     /usr/local/bin/mp $@
#   )
# }

import argparse
import inspect
import logging
from mptools.compile import compile_to_final_crowdanki_json_in_project_root
from mptools.raw_tools import fill_empty_guids

parser = argparse.ArgumentParser(description='tool for working with Memorize Python')
parser.add_argument('mode', nargs="?", choices=['compile', 'guid'])
parser.add_argument('-v', action="count", default=0, help="additive verbosity")
args = parser.parse_args()

if args.v >= 2:
    logging.basicConfig(level=logging.DEBUG)
elif args.v >= 1:
    logging.basicConfig(level=logging.INFO)


def debug(message):
    caller_info = 'caller : {} : '.format(inspect.stack()[1][3])
    logging.debug(caller_info + str(message))


def do_compile():
    compile_to_final_crowdanki_json_in_project_root()


if args.mode == 'compile':
    do_compile()
elif args.mode == 'guid':
    fill_empty_guids()
else:
    parser.print_help()
