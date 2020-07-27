from mamba import context, describe, it
from expects import expect, equal, be_false, be_true

from bee import Map, Position

with describe("map") as self:
    with it("checks positions within given size"):
        expect(Map(5, 5).check(Position(0, 0))).to(be_true)
        expect(Map(10, 10).check(Position(10, 10))).to(be_false)
        expect(Map(11, 11).check(Position(10, 10))).to(be_true)

    # with it('')
