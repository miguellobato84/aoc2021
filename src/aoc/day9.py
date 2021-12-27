import argparse
import logging
import sys
from numpy.core.fromnumeric import shape

from numpy.lib.arraysetops import union1d, unique
from numpy.lib.index_tricks import c_

from aoc import __version__
import numpy as np
import collections

__author__ = "Miguel Á. Lobato"
__copyright__ = "Miguel Á. Lobato"
__license__ = "MIT"

_logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

MAX = 9

def find_peaks(lines):
    def min_around(x, y):
        bound_x = lines.shape[0]-1
        bound_y = lines.shape[1]-1
        a,b,c,d = lines[x-1, y] if x>0 else MAX, lines[x, y-1] if y > 0 else MAX, lines[x+1, y] if x < bound_x else MAX, lines[x, y+1] if y < bound_y else MAX
        return min(a,b,c,d)

    def is_lower_others(x,y):
        return lines[x,y] < min_around(x,y)
    
    for x in range(lines.shape[0]):
        yield [1 if is_lower_others(x,y) else 0 for y in range(lines.shape[1])]

def get_lowest_for(x,y,lines,lowest):
    logging.debug(f"get_lowest_for({x}, {y}) -> start")
    bound_x = lines.shape[0]-1
    bound_y = lines.shape[1]-1
    current_val = lines[x,y]

    if (x,y) in lowest:
        logging.debug(f"get_lowest_for({x}, {y}) -> lowest point")
        return (x,y)
    elif x<0 or x>bound_x or y<0 or y>bound_y or lines[x,y] == MAX:
        logging.debug(f"get_lowest_for({x}, {y}) -> out of scope")
        return None
    else:
        top = (x-1,y) if x>0 and lines[x-1,y] < current_val else None
        down = (x+1,y) if x<bound_x and lines[x+1,y] < current_val else None
        left = (x,y-1) if y>0 and lines[x,y-1] < current_val else None
        right = (x,y+1) if y<bound_y and lines[x,y+1] < current_val else None
        logging.debug(f"get_lowest_for({x}, {y}) -> {[top, down, left, right]}")
        directions = [get_lowest_for(v[0],v[1],lines,lowest) for v in [top,down,left,right] if v]
        directions = list(filter(lambda x:x is not None, directions))
        return directions[0] if len(directions) > 0 else None

def ex1(lines):
    t = np.array(list(find_peaks(lines)))
    return np.sum(t * lines) + np.sum(t)

def ex2(lines):
    t = np.array(list(find_peaks(lines)))
    lowest = {(x,y):0 for x,y in np.argwhere(t==1)}
    for x in range(lines.shape[0]):
        for y in range(lines.shape[1]):
            if lines[x,y] < MAX:
                c_x,c_y = get_lowest_for(x,y,lines,lowest)
                lowest[(c_x,c_y)] += 1

    results = sorted(lowest.values(), reverse=True)
    return results[0] * results[1] * results[2]
