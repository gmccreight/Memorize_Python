import json
import copy
from string import Template
from pathlib import Path
import random
import re
import logging

# I really wanted to just copy some of Anki's code for generating a guid here,
# but our license (BSD) is more permissive than Anki's (AGPL) so I'm just going
# to throw some random characters together.  I realize this is tricky, because
# it needs to be a clean-room implementation, which is a shame, because I bet
# the Anki code is pretty good!


def empty_guid_replace(match):
    return '"guid": "{}",'.format(guid())


def fill_empty_guids():
    for f in json_files():
        logging.debug(f"checking the guids in {f}")
        d = f.read_text()
        before = d
        d = re.sub(r'"guid": "",', empty_guid_replace, d)
        after = d
        f.write_text(d)
        if after != before:
            logging.debug(f"added one or more guids to {f}")


def guid():
    f = []
    for i in ((48, 10), (97, 26), (65, 26)):
        f.extend([chr(i) for i in range(i[0], i[0] + i[1])])
    f = f * 10
    return "".join(random.sample(f, 10))


def json_files():
    return (Path(__file__).parent.parent / "data/raw").rglob("*.json")
