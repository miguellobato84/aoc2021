import pytest

from aoc.day1 import ex1, ex2

__author__ = "Miguel Á. Lobato"
__copyright__ = "Miguel Á. Lobato"
__license__ = "MIT"


def test_ex1():
    assert ex1([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]) == 7

    with open('./tests/inputs/day1.txt') as f:
        lines = list(map(lambda x: int(x), f.readlines()))
        assert(ex1(lines) == 1387)


def test_ex2():
    assert ex2([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]) == 5

    with open('./tests/inputs/day1.txt') as f:
        lines = list(map(lambda x: int(x), f.readlines()))
        assert(ex2(lines) == 1362)
