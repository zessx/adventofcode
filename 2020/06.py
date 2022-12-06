#!/usr/bin/env python3

from functools import reduce
from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self):
    self.groups_inc = []
    self.groups_exc = []
    current_inc = []
    current_exc = []
    for line in self.input.splitlines():
      if line == b"":
        self.groups_inc.append(current_inc)
        self.groups_exc.append(reduce(lambda a, b: list(set(a).intersection(b)), current_exc))
        current_inc = []
        current_exc = []
      else:
        current_inc.extend(list(line))
        current_exc.append(list(line))
    self.groups_inc.append(current_inc)
    self.groups_exc.append(reduce(lambda a, b: list(set(a).intersection(b)), current_exc))


  def solve1(self):
    self.calculate()
    return sum([len(set(group)) for group in self.groups_inc])

  def solve2(self):
    self.calculate()
    return sum([len(set(group)) for group in self.groups_exc])
