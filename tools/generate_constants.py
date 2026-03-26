

#!/usr/bin/env python3
"""
Generate constants.py from JSON data extracted by wows-sandbox.

Usage:
    python3 generate_constants.py extracted.json [output.py]
    cat extracted.json | python3 generate_constants.py -
"""
import json
import re
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


def camel_to_upper(name):
    """Convert CamelCase to UPPER_SNAKE_CASE: 'InProgress' -> 'IN_PROGRESS'."""
    s = re.sub(r'(?<=[a-z0-9])([A-Z])', r'_\1', name)
    return s.upper()


def sort_by_value(mapping):
    """Sort a dict by its values, return (key, value) pairs."""
    return sorted(mapping.items(), key=lambda x: x[1])


def dictsort_by_value(mapping):
    """Sort a dict by its values, return (key, value) pairs."""
    return sorted(mapping.items(), key=lambda x: x[1])


def dictsort_by_int_key(mapping):
    """Sort a dict by integer keys, return (int_key, value) pairs."""
    return sorted(mapping.items(), key=lambda x: int(x[0]))


def pformat(obj):
    """Format a Python object as a repr string with int keys where appropriate."""
    if isinstance(obj, dict):
        items = []
        for k, v in obj.items():
            try:
                k = int(k)
            except (ValueError, TypeError):
                pass
            items.append(f'{k!r}: {v!r}')
        return '{' + ', '.join(items) + '}'
    return repr(obj)


def format_property_map(mapping, name):
    """Format an id-to-name property map with line wrapping."""
    int_map = {int(k): v for k, v in mapping.items()}
    items = [f'{k}: {v!r}' for k, v in sorted(int_map.items())]

    lines = []
    current = f'{name} = {{'
    indent = ' ' * (len(name) + 4)
    for i, item in enumerate(items):
        sep = ', ' if i < len(items) - 1 else '}'
        addition = item + sep
        if len(current) + len(addition) > 105:
            lines.append(current)
            current = indent + addition
        else:
            current += addition
    lines.append(current)
    return '\n'.join(lines)


def format_tuple(items, name):
    """Format a list of strings as a named tuple constant with line wrapping."""
    if not items:
        return f'{name} = ()'
    lines = [f'{name} = (']
    current = '    '
    for i, item in enumerate(items):
        sep = ', ' if i < len(items) - 1 else ')'
        addition = f'{item!r}{sep}'
        if len(current) + len(addition) > 105:
            lines.append(current)
            current = '    ' + addition
        else:
            current += addition
    lines.append(current)
    return '\n'.join(lines)


def format_skill_lines(mapping):
    """Format skill ID-to-name dict as wrapped lines of key: value pairs."""
    int_map = {int(k): v for k, v in mapping.items()}
    lines = []
    current = ''
    for k, v in sorted(int_map.items()):
        item = f'{k}: {v!r}, '
        if len(current) + len(item) > 101:
            lines.append(current.rstrip())
            current = item
        else:
            current += item
    if current.strip():
        lines.append(current.rstrip())
    return lines


def create_env():
    template_dir = Path(__file__).parent
    env = Environment(
        loader=FileSystemLoader(template_dir),
        keep_trailing_newline=True,
        lstrip_blocks=True,
        trim_blocks=True,
    )
    env.filters['camel_to_upper'] = camel_to_upper
    env.filters['sort_by_value'] = sort_by_value
    env.filters['dictsort_by_value'] = dictsort_by_value
    env.filters['dictsort_by_int_key'] = dictsort_by_int_key
    env.filters['pformat'] = pformat
    env.filters['format_property_map'] = format_property_map
    env.filters['format_skill_lines'] = format_skill_lines
    env.filters['format_tuple'] = format_tuple
    return env


def main():
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <extracted.json | -> [output.py]',
              file=sys.stderr)
        sys.exit(1)

    input_path = sys.argv[1]
    if input_path == '-':
        raw = json.load(sys.stdin)
    else:
        with open(input_path) as f:
            raw = json.load(f)

    if 'errors' in raw and raw['errors']:
        print('Extraction warnings:', file=sys.stderr)
        for err in raw['errors']:
            print(f'  - {err}', file=sys.stderr)

    data = raw.get('data', raw)

    env = create_env()
    template = env.get_template('constants.py.j2')
    output = template.render(**data)

    if len(sys.argv) > 2:
        Path(sys.argv[2]).write_text(output)
    else:
        print(output)


if __name__ == '__main__':
    main()
