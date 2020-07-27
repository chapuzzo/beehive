from mamba import context, describe, it
from expects import expect, equal, be_false, be_true, have_property

from bee import Bee
from position import Position
from environment import Environment

with describe(Environment) as self:
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

        positions = [Position(*coords) for coords in flowers]
        env = Environment(flowers=positions)

        expect(env.is_flower(positions[0])).to(be_true)
        expect(env.is_flower(Position(0, 0))).to(be_false)


with describe(Bee) as self:
    with describe("movement"):
        with it("moves if no known environment"):
            bee = Bee("#1")
            result = bee.move("x", 5)
            expect(result).to(be_true)

        with it("updates postiion when moving"):
            bee = Bee("#2")
            result = bee.move("x", 5)
            expect(bee.position).to(equal(Position(5, 0)))

        with it("refuses to move outside known environment"):
            bee = Bee("#3", Environment(5, 5))
            result = bee.move("x", 10)
            expect(result).to(be_false)
            expect(bee.position).to(equal(Position()))

        with it("refuses to move in an unknown axis"):
            bee = Bee("#y", Environment(5, 5))
            result = bee.move("z", 3)
            expect(result).to(be_false)
            expect(bee.position).to(equal(Position()))
