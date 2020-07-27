from position import Position


class Environment:
    def __init__(self, width=10, height=10, flowers=None):
        self.flowers = flowers
        self.width = width
        self.height = height

    def check(self, position: Position) -> bool:
        if 0 <= position.x < self.width and 0 <= position.y < self.height:
            return True
        return False

    def is_flower(self, position: Position) -> bool:
        return position in self.flowers
