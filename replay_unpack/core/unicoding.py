from typing import Any


def unicodize(value: Any):
    """
    Recursively try to decode bytes as utf-8.
    """
    if isinstance(value, bytes):
        try:
            value = value.decode('utf-8')
        except UnicodeDecodeError:
            pass
    elif isinstance(value, list):
        value = [unicodize(i) for i in value]

    elif isinstance(value, dict):
        value = {unicodize(k): unicodize(v)
                 for k, v in value.items()}

    return value
