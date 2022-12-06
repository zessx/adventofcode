#!/usr/bin/env python3

from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self):
    self.items = list(map(lambda x: int(x), self.input.splitlines()))

  def solve1(self):
    self.calculate()
    return len([i for i in range(len(self.items) - 1) if self.items[i] < self.items[i+1]])

  def solve2(self):
    self.calculate()
    return len([i for i in range(len(self.items) - 3) if sum(self.items[i:i+3]) < sum(self.items[i+1:i+4])])
