from mamba import context, describe, it
from expects import expect, equal, be_false, be_true, have_property

from position import Position
from environment import Environment

with describe("environment") as self:
    with it("has default size"):
        expect(Environment()).to(have_property("width", 10))
        expect(Environment()).to(have_property("height", 10))

    with it("checks positions within given size"):
        expect(Environment(5, 5).check(Position(0, 0))).to(be_true)
        expect(Environment(10, 10).check(Position(10, 10))).to(be_false)
        expect(Environment(11, 11).check(Position(10, 10))).to(be_true)

    with it("gives information about known flowers"):
        flowers = [
            (5, 5),
            (7, 3),
        ]

        import sys

        print(sys.version_info)

        positions = [Position(*coords) for coords in flowers]
        env = Environment(flowers=positions)

        expect(env.is_flower(positions[0])).to(be_true)
        expect(env.is_flower(Position(0, 0))).to(be_false)
