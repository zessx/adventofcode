#!/usr/bin/env python3

from lib.solver import BaseSolver
from re import match

class Solver(BaseSolver):
  def calculate(self, quantifier: str = ""):
    return sum(i \
      for line in self.input.split(b",") \
      for a, b in [map(int, line.split(b"-"))] \
      for i in range(a, b + 1) \
      if match(rf"^(.+)\1{quantifier}$", str(i)))

  def solve1(self):
    return self.calculate()

  def solve2(self):
    return self.calculate(quantifier = "+")
