import argparse
import logging
import sys

from aoc import __version__
import numpy as np

__author__ = "Miguel Á. Lobato"
__copyright__ = "Miguel Á. Lobato"
__license__ = "MIT"

_logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def is_card_winner(numbers, card):
    t_mark_success = np.frompyfunc(lambda x: 1 if x in numbers else 0, 1, 1)
    winner = max(np.sum(t_mark_success(card), axis=0).max(),
                 np.sum(t_mark_success(card), axis=1).max()) == 5

    if winner:
        _logger.debug(f"We have a winner: numbers={numbers}")
        _logger.debug("Card:")
        _logger.debug(card)
        _logger.debug("Checks:")
        _logger.debug(t_mark_success(card))
    return winner


def get_card_points(numbers, card):
    t = np.frompyfunc(lambda x: x if x not in numbers else 0, 1, 1)
    _logger.debug("Not marked numbers:")
    _logger.debug(t(card))
    a = np.sum(t(card))
    b = numbers[-1]
    _logger.debug(f"Points: {a}*{b}={a*b}")
    return a*b


def ex1(numbers, cards):
    numbers = [numbers[0:x+1] for x in range(len(numbers))]
    for n in numbers:
        winner_cards = [card for card in cards if is_card_winner(n, card)]
        if len(winner_cards) > 0:
            return get_card_points(n, winner_cards[0])
    return 0


def ex2(numbers, cards):
    numbers = [numbers[0:x+1] for x in range(len(numbers))]
    while True:
        for n in numbers:
            if len(cards) > 1:
                cards = list(filter(lambda x: not is_card_winner(n, x), cards))
                _logger.debug(f"There are {len(cards)} remaining cards. Numbers are {n}")
            else:
                if is_card_winner(n, cards[0]):
                    return get_card_points(n, cards[0])
