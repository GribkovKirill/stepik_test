<<<<<<< HEAD
class Matrix:
    def __init__(self, rows: int, cols: int, value: int = 0):
        self.rows = rows
        self.cols = cols
        if isinstance(value, int):
            self.matrix = [
                [value for i in range(self.cols)]
                for j
                in range(self.rows)
            ]

    def __str__(self) -> str:
        rows = map(lambda x: ' '.join(map(str, x)), self.matrix)
        return '\n'.join(rows)

    def __repr__(self) -> str:
        return f'Matrix({self.rows}, {self.cols})'

    def __pos__(self):
        new_obj = Matrix(self.rows, self.cols)
        new_obj.matrix = self.matrix
        return new_obj

    def __neg__(self):
        new_obj = Matrix(self.rows, self.cols)
        new_obj.matrix = [
                [self.matrix[j][i] * -1 for i in range(self.cols)]
                for j
                in range(self.rows)
            ]
        return new_obj

    def __invert__(self):
        new_obj = Matrix(self.cols, self.rows)
        new_obj.matrix = [
                [self.matrix[i][j] for i in range(self.rows)]
                for j
                in range(self.cols)
            ]
        return new_obj

    def __round__(self, n = None):
        new_obj = Matrix(self.rows, self.cols)
        if n is None:
            new_obj.matrix = [
                [round(self.matrix[j][i]) for i in range(self.cols)]
                for j
                in range(self.rows)
            ]
            return new_obj
        new_obj.matrix = [
                [round(self.matrix[j][i], n)  for i in range(self.cols)]
                for j
                in range(self.rows)
            ]
        return new_obj

    def get_value(self, row: int, col: int) -> int | float:
        return self.matrix[row][col]

    def set_value(self, row: int, col: int, value: int | float):
        self.matrix[row][col] = value
=======
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
>>>>>>> 9f734edaddd3e7b962c36d51558775fb954bc0fc
