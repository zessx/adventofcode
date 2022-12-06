#!/usr/bin/env python3

from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self):
    self.items = [int(i) for i in self.input.split(b",")]

  def solve1(self):
    self.calculate()
    return min([sum([abs(i - a) for i in self.items]) for a in range(min(self.items), max(self.items))])

  def solve2(self):
    self.calculate()
    return min([sum([int(abs(i - a) * (abs(i - a) + 1) / 2) for i in self.items]) for a in range(min(self.items), max(self.items))])
