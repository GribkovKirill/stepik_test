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
