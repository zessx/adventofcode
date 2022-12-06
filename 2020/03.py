#!/usr/bin/env python3

from lib.solver import BaseSolver
from math import ceil, floor

class Solver(BaseSolver):
  def count_trees(self, shiftr: int, shiftd: int) -> int:
    lines = self.input.splitlines()
    height = len(lines)
    segment_width = len(lines[0])
    required_width = height * shiftr + 1
    required_segments = ceil(required_width / segment_width)
    lines_extended = list(map(lambda line: line * required_segments, lines))
    return len([1 for i in range(shiftd, height, shiftd) if chr(lines_extended[i][floor(i / shiftd) * shiftr]) == "#"])

  def solve1(self):
    return self.count_trees(3, 1)

  def solve2(self):
    return self.count_trees(1, 1) \
      * self.count_trees(3, 1) \
      * self.count_trees(5, 1) \
      * self.count_trees(7, 1) \
      * self.count_trees(1, 2)
