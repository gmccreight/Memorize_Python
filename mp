#!/usr/bin/env python3

# Symlink this file into a place in your path for easy commands.

# In your bash aliases, you should consider doing something like this:

# function mp {
#   if [ "$1" = "cd" ]; then
#     cd ~/memorize_python
#     return
#   fi
#
#   (
#     cd ~/memorize_python
#     /usr/local/bin/mp $@
#   )
# }

import argparse
import logging
import os

parser = argparse.ArgumentParser(description='tool for working with mp')
parser.add_argument('command')
parser.add_argument('-v', action="count", default=0)
args = parser.parse_args()

if args.v == 1:
    logging.basicConfig(level=logging.INFO)
elif args.v == 2:
    logging.basicConfig(level=logging.DEBUG)


def run(command):
    logging.debug("running: " + command)
    os.system(command)

if args.command == 'e':
    run("$EDITOR " + os.path.realpath(__file__))

else:
    logging.error('command {} not found'.format(args.command))
