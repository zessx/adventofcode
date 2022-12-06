#!/usr/bin/env python3

from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self):
    self.items = list(map(lambda x: int(x), self.input.splitlines()))

  def solve1(self):
    self.calculate()

    shift_3 = int(len(list(set(range(1, max(self.items) + 1)) - set(self.items))) / 2) + 1
    shift_1 = len(self.items) - shift_3 + 1
    return shift_1 * shift_3
