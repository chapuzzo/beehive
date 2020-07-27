class Position:
    __slots__ = ("x", "y")

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Position x={}, y={}>".format(self.x, self.y)

    def distance(self, other: "Position") -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return all(
            getattr(self, axis) == getattr(other, axis) for axis in self.__slots__
        )
