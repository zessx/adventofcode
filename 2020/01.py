#!/usr/bin/env python3

from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self):
    self.items = list(map(lambda x: int(x), self.input.splitlines()))

  def solve1(self):
    self.calculate()

    half = 2020 / 2
    half_items = [item for item in self.items if item <= half]
    matching_items = [item for item in self.items if 2020 - item in half_items]
    return matching_items[0] * (2020 - matching_items[0])

  def solve2(self):
    self.calculate()

    third = 2020 / 3
    third_items = [item for item in self.items if item <= third]
    for third_item in third_items:
      matching_items = [item for item in self.items if 2020 - third_item - item in self.items]
      if len(matching_items) > 0:
        return matching_items[0] * third_item * (2020 - matching_items[0] - third_item)

