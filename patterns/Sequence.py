from typing import Any


class Sequence:
    def __len__(self):
        return len(Any)

    def __getitem__(self, key):
        return self[key]

    def __setitem__(self, key, value):
        self[key] = value

    def __delitem__(self, key):
        del self[key]

    def __contains__(self, item):
        return item in self

    def __iter__(self):
        yield from self
