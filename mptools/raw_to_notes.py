import json
import copy
from string import Template
from pathlib import Path


def file_to_notes(pathstring):
    d = None
    with open(pathstring, 'r') as f:
        d = json.load(f)
    notes = annotated_notes_from_data(d)
    final_json = annotated_notes_to_final_json(notes)
    return final_json


def val_or_action_data(d):
    """Return everything in the root, except keys containing __"""
    return dict([(x, d[x]) for x in d if x.find('__') != 0])


def rollup(data, new):
    result = copy.deepcopy(data)

    # new and pure overrides
    for x in val_or_action_data(new):
        if x.find("__") == -1:
            result[x] = new[x]

    # actions like plusequal, extend, etc
    for x in val_or_action_data(new):
        if x.find("__") > 0:
            key, action = x.split("__")
            if action == "plusequal":
                result[key] += new[x]
            elif action == "extend":
                result[key].extend(new[x])

    return result


def annotated_notes_from_data(d):
    result = []

    l1 = val_or_action_data(d)

    for section in d["__sections"]:
        l2 = val_or_action_data(section)
        for note in section["__notes"]:
            l3 = val_or_action_data(note)
            note = {
                "raw": (l1.copy(), l2.copy(), l3.copy()),
                "rollup": l1.copy()
            }
            result.append(note)

    for note in result:
        for i in range(1, len(note["raw"])):
            note["rollup"] = rollup(note["rollup"], note["raw"][i])

    return result


def annotated_notes_to_final_json(notes):
    result = []
    template_text = (Path(__file__).parent.parent / 'templates/single_note.json').read_text()
    template = Template(template_text)
    for note in notes:
        note["rollup"]["tags"] = json.dumps(note["rollup"]["tags"])
        result.append(template.substitute(note["rollup"]))
    all_json = "[" + ",".join(result) + "]"
    return json.dumps(json.loads(all_json), indent=4, sort_keys=True)
