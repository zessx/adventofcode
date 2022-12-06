#!/usr/bin/env python3

from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self):
    self.items = list(map(lambda x: int(x), self.input.splitlines()))
    self.invalid = [self.items[i] for i in range(25, len(self.items) - 25) if not self.check_validity(self.items[i-25:i], self.items[i])][0]

  def check_validity(self, values, input) -> bool:
    half_items = [item for item in values if item <= input / 2]
    return len([item for item in values if input - item in half_items]) > 0

  def solve1(self):
    self.calculate()
    return self.invalid

  def solve2(self):
    self.calculate()

    l = 0
    while l < len(self.items) - 1:
      r = [self.items[i:l+1] for i in range(len(self.items)) if sum(self.items[i:l+1]) == self.invalid]
      if len(r) > 0:
        return min(r[0]) + max(r[0])
      l += 1
