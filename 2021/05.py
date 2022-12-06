#!/usr/bin/env python3

import re
from itertools import chain
from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self):
    self.items = self.input.splitlines()

    size = 1000
    self.map_hv = [[0 for _ in range(size)] for _ in range(size)]
    self.map_all = [[0 for _ in range(size)] for _ in range(size)]
    for line in self.items:
      x1, y1, x2, y2 = [int(i) for i in re.match(rb"^(\d+),(\d+) -> (\d+),(\d+)$", line).groups()]
      if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
          self.map_hv[x1][i] += 1
          self.map_all[x1][i] += 1
      elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
          self.map_hv[i][y1] += 1
          self.map_all[i][y1] += 1
      else:
        y = y1 if x2 > x1 else y2
        for x in range(min(x1, x2), max(x1, x2) + 1):
          self.map_all[x][y] += 1
          y += (1 if y2 > y1 else -1) * (1 if x2 > x1 else -1)

  def solve1(self):
    self.calculate()
    return len([i for i in list(chain.from_iterable(self.map_hv)) if i > 1])

  def solve2(self):
    self.calculate()
    return len([i for i in list(chain.from_iterable(self.map_all)) if i > 1])
