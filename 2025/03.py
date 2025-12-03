#!/usr/bin/env python3

from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self, digits: int):
    joltages = []
    for line in self.input.splitlines():
      batteries = [int(b) for b in line.decode()]
      joltage_digits = []
      search_from = 0
      search_until = len(batteries) - digits + 1
      for _ in range(digits):
        joltage_digits.append(max(batteries[search_from:search_until]))
        search_from += batteries[search_from:search_until].index(joltage_digits[-1]) + 1
        search_until += 1
      joltages.append(int(''.join([str(d) for d in joltage_digits])))
    return sum(joltages)

  def solve1(self):
    return self.calculate(2)

  def solve2(self):
    return self.calculate(12)
