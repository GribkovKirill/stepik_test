class Queue:
    def __init__(self, *args):
        self.args = list(args)

    def __str__(self) -> str:
        return ' -> '.join(map(str, self.args))

    def add(self, *args):
        self.args += list(args)

    def pop(self):
        if self.args:
            return self.args.pop(0)
        else:
            return None

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.args == other.args
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Queue):
            return Queue(*(self.args + other.args))
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Queue):
            self.args += other.args
            return self
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int):
            if other < len(self.args):
                return Queue(*self.args[other:])
            else:
                return Queue()
        return NotImplemented
