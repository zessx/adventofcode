#!/usr/bin/env python3

from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self):
    self.plays = self.input.splitlines()

  def solve1(self):
    self.calculate()

    def score(opp, own) -> int:
      score = ord(own) - 87
      if (ord(own) - ord(opp)) == 23:
        score += 3
      elif (ord(own) - ord(opp)) in [24, 21]:
        score += 6
      return score

    return sum([score(*p.split(b' ')) for p in self.plays])

  def solve2(self):
    self.calculate()

    def score(opp, expected_result) -> int:
      if ord(expected_result) == 89:
        return 3 + ord(opp) - 64
      if ord(expected_result) == 90:
        return 6 + (ord(opp) - 65 + 1) % 3 + 1
      return (ord(opp) - 65 - 1) % 3 + 1

    return sum([score(*p.split(b' ')) for p in self.plays])
