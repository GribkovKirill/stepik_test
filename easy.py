class ColoredPoint:
    def __init__(
        self, x: int | float,
        y: int | float,
        color: str
    ):
        self._x = x
        self._y = y
        self._color = color

    def __repr__(self):
        return f'ColoredPoint{repr(self._atributes)}'

    def __eq__(self, other) -> bool:
        if isinstance(other, ColoredPoint):
            return self._atributes == other._atributes
        return NotImplemented

    def __hash__(self):
        return hash(self._atributes)

    @property
    def x(self) -> int | float:
        return self._x

    @property
    def y(self) -> int | float:
        return self._y

    @property
    def color(self) -> str:
        return self._color

    @property
    def _atributes(self) -> tuple:
        return self.x, self.y, self.color
