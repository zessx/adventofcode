#!/usr/bin/env python3

from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self):
    self.items = [int(i) for i in self.input.split(b",")]

  def calc_fishes(self, fishes, days: int) -> int:
    items = [fishes.count(i) for i in range(10)]
    for i in range(days):
      zero = items[0]
      items = items[1:] + [0]
      items[6] += zero
      items[8] += zero
    return sum(items)

  def solve1(self):
    self.calculate()
    return self.calc_fishes(self.items.copy(), 80)

  def solve2(self):
    self.calculate()
    return self.calc_fishes(self.items.copy(), 256)
