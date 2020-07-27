from typing import Optional


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


class Map:
    def __init__(self, width=10, height=10, flowers=None):
        self.width = width
        self.height = height

    def check(self, position: Position) -> bool:
        if 0 <= position.x < self.width and 0 <= position.y < self.height:
            return True
        return False

    # def __repr__(self):


class Bee:
    def __init__(self, name, map: Optional[Map] = None, position=None):
        self.name = name
        self.position = position if position is not None else Position()
        self.map = map

    def __repr__(self) -> str:
        return "<bee {}>".format(self.__dict__)

    def move(self, direction, amount) -> bool:
        delta = Position(**{direction: amount})
        new_position = self.position + delta

        if self.map is None:
            return True

        if self.map.check(new_position):
            self.position = new_position
            return True
        else:
            return False
            # setattr(self.position, direction, getattr(self.position, direction) + amount)

    def distance(self, other: "Bee") -> int:
        return self.position.distance(other.position)


class Hive:
    pass


def test_all():
    m = Map(5, 7)
    bee = Bee("Luis", m)
    print(bee)
    bee.move("x", 5)
    print(bee.distance(Bee("x")))
    bee.move("x", -5)
    print(bee)


if __name__ == "__main__":
    test_all()
