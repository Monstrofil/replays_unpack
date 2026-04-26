"""Tolerant loader for the game's GameParams.data blob.

GameParams.data is bytes-reversed zlib-compressed pickle; the pickle references
GameParams.GPData (and a few sibling classes) that don't exist outside the game
client. We don't actually need those classes' methods - we only read attributes
- so we stub unknown classes with ones that accept any state, then the loaded
tree behaves like a tower of plain objects with `__dict__` attributes.
"""
import io
import pickle
import zlib


class _GPItem:
    def __setstate__(self, state):
        if isinstance(state, dict):
            self.__dict__.update(state)
        else:
            self._state = state


class _StubModule:
    def __init__(self, name):
        self._name = name

    def __getattr__(self, item):
        return type(item, (_GPItem,),
                    {'__module__': self._name, '__qualname__': item})


class _Tolerant(pickle.Unpickler):
    def find_class(self, module, name):
        try:
            return super().find_class(module, name)
        except Exception:
            return getattr(_StubModule(module), name)


def load_gameparams(path):
    """Return the full {region: {index: GPItem-stub}} mapping."""
    with open(path, 'rb') as f:
        raw = f.read()
    pickled = zlib.decompress(raw[::-1])
    return _Tolerant(io.BytesIO(pickled), encoding='latin1').load()
