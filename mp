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
import inspect
import json
import logging
import os
import shutil

parser = argparse.ArgumentParser(description='tool for working with mp')
parser.add_argument('-v', action="count", default=0)
args = parser.parse_args()

if args.v >= 2:
    logging.basicConfig(level=logging.DEBUG)
elif args.v >= 1:
    logging.basicConfig(level=logging.INFO)


def debug(message):
    caller_info = 'caller : {} : '.format(inspect.stack()[1][3])
    logging.debug(caller_info + str(message))


def raw_data_files():
    raw_data_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "data/raw"
    )
    debug(raw_data_path)
    results = []
    for i in os.walk(raw_data_path):
        files = i[2]
        for f in files:
            if f.endswith('.json'):
                results.append(os.path.join(i[0], f))
    return results


def generated_dir_path():
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "generated"
    )


def ensure_generated_dir_and_clean():
    try:
        os.mkdir(generated_dir_path())
    except FileExistsError:
        pass

    shutil.rmtree(generated_dir_path())
    os.mkdir(generated_dir_path())


ensure_generated_dir_and_clean()
files = raw_data_files()

for json_file in files:
    debug(json_file)
    with open(json_file) as json_source:
        d = json.load(json_source)
        output_path = os.path.join(generated_dir_path(), d['slug'] + '.html')
        with open(output_path, 'x') as f:
            f.write(d['source'])




