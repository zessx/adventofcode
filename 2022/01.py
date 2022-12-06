#!/usr/bin/env python3

from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self):
    self.calories = []
    current_elf = 0
    for line in self.input.splitlines():
      if line == b'':
        self.calories.append(current_elf)
        current_elf = 0
      else:
        current_elf += int(line)


  def solve1(self):
    self.calculate()
    return max(self.calories)

  def solve2(self):
    self.calculate()
    return sum(sorted(self.calories, reverse=True)[:3])
