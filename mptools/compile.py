import json
from pathlib import Path
from mptools.raw_to_notes import file_to_notes
from mptools.notes_into_final import add_notes_to_template


def compile_to_final_crowdanki_json_in_project_root():

    f = str((Path(__file__).parent.parent / "data/raw/built-in-funcs.json").resolve())

    notes_json_text = file_to_notes(f)
    add_notes_to_template(notes_json_text)
