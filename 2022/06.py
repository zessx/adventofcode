#!/usr/bin/env python3

from lib.solver import BaseSolver

class Solver(BaseSolver):
  def solve1(self):
    for i in range(len(self.input) - 4):
      if len(set(self.input[i:i+4])) == len(self.input[i:i+4]):
        return i + 4

  def solve2(self):
    for i in range(len(self.input) - 14):
      if len(set(self.input[i:i+14])) == len(self.input[i:i+14]):
        return i + 14
