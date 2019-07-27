import json
from pathlib import Path
from mptools.raw_to_notes import file_to_notes
from mptools.notes_into_final import add_notes_to_template


def compile_to_final_crowdanki_json_in_project_root():
    all_notes = []
    for f in raw_json_files():
        f = str(f)
        all_notes.extend(file_to_notes(f))
    json_block = all_notes_to_json_block(all_notes)
    add_notes_to_template(json_block)


def raw_json_files():
    return (Path(__file__).parent.parent / "data/raw").rglob("*.json")


def all_notes_to_json_block(notes):
    all_json = "[" + ",".join(notes) + "]"
    return json.dumps(json.loads(all_json), indent=4, sort_keys=True)
