import json
from string import Template
from pathlib import Path


def add_notes_to_template(notes_json_text):
    template_text = (Path(__file__).parent.parent / 'templates/Memorize_Python.json').read_text()
    dest = Path(__file__).parent.parent / 'Memorize_Python.json'

    template = Template(template_text)
    indented_notes = "".join(["    " + x for x in notes_json_text.splitlines(keepends=True)[1:-1]])
    result = template.substitute({"notes": indented_notes})

    dest.unlink()
    dest.write_text(result)

    # Load the output just to make sure it made a sane file
    json.loads(dest.read_text())
