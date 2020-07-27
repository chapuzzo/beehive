from typing import Optional

from environment import Environment
from position import Position


class Bee:
    def __init__(self, name, env: Optional[Environment] = None, position=None):
        self.name = name
        self.position = position if position is not None else Position()
        self.env = env

    def __repr__(self) -> str:
        return "<bee {}>".format(self.__dict__)

    def move(self, direction, amount) -> bool:
        delta = Position(**{direction: amount})
        new_position = self.position + delta

        if self.env is None:
            return True

        if self.env.check(new_position):
            self.position = new_position
            return True
        else:
            return False

    def distance(self, other: "Bee") -> int:
        return self.position.distance(other.position)


class Hive:
    pass
