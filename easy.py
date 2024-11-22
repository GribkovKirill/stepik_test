from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, version: str):
        version: list = version.split('.')
        while len(version) < 3:
            version.append('0')
        self.version = '.'.join(version)
        self.numbers = list(map(int, version))

    def __str__(self) -> str:
        return self.version

    def __repr__(self) -> str:
        return f'Version({repr(self.version)})'

    def __eq__(self, other):
        if isinstance(other, Version):
            return self.numbers == other.numbers
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Version):
            if self.numbers[0] < other.numbers[0]:
                return self.numbers[0] < other.numbers[0]
            elif self.numbers[0] == other.numbers[0]:
                if self.numbers[1] < other.numbers[1]:
                    return self.numbers[1] < other.numbers[1]
                elif self.numbers[1] == other.numbers[1]:
                    return self.numbers[2] < other.numbers[2]
        return NotImplemented
