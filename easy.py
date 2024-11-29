from typing import Any


class AttrsNumberObject:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            self.__setattr__(name, value)

    def __getattr__(self, name):
        return len(self.__dict__) + 1

music_group = AttrsNumberObject(name='Silent Poets', genre='acid jazz')

print(music_group.attrs_num)
