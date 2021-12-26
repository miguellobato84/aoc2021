import pytest

from aoc.day2 import ex1, ex2

__author__ = "Miguel Á. Lobato"
__copyright__ = "Miguel Á. Lobato"
__license__ = "MIT"


def test_ex1():
    assert ex1([["forward", 5], ["down", 5], ["forward", 8], ["up", 3], ["down", 8], ["forward", 2]]) == 150

    with open('./tests/inputs/day2.txt') as f:
        lines = list(map(lambda x: [x.split(" ")[0], int(x.split(" ")[1])], f.readlines()))
        print(f"Solution of day 2, exercise 1 is {ex1(lines)}")
        assert(ex1(lines) == 1250395)


def test_ex2():
    assert ex2([["forward", 5], ["down", 5], ["forward", 8], ["up", 3], ["down", 8], ["forward", 2]]) == 900

    with open('./tests/inputs/day2.txt') as f:
        lines = list(map(lambda x: [x.split(" ")[0], int(x.split(" ")[1])], f.readlines()))
        print(f"Solution of day 2, exercise 2 is {ex2(lines)}")
        assert(ex2(lines) == 1451210346)
