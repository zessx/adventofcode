#!/usr/bin/env python3

from lib.solver import BaseSolver
from typing import Counter

class Solver(BaseSolver):
  def calculate(self):
    self.items = [l for l in self.input.decode("utf-8").splitlines()]

  def solve(self, solve_step: int):
    self.calculate()

    entry = self.items[0]
    rules = {j[0]: j[1] for j in [i.split(" -> ") for i in self.items if "->" in i]}
    counters = {j[0]: 0 for j in [i.split(" -> ") for i in self.items if "->" in i]}

    for i in range(len(entry) - 1):
      counters[entry[i:i+2]] += 1

    for step in range(1, 11 if solve_step == 1 else 41):
      new_counters = counters.copy()
      for c in counters:
        if counters[c] > 0:
          new_counters[c[0] + rules[c]] += counters[c]
          new_counters[rules[c] + c[1]] += counters[c]
          new_counters[c]= max(0, new_counters[c] - counters[c])
      counters = new_counters.copy()

      if step in (10, 40):
        letter_counters = Counter()
        letter_counters.update({x:0 for x in ["B", "C", "H", "N"]})
        letter_counters.update({x:1 for x in [entry[0], entry[-1]]})
        for c in counters:
          letter_counters[c[0]] += counters[c]
          letter_counters[c[1]] += counters[c]

        results = letter_counters.most_common()

    return int(results[0][1] / 2 - results[-1][1] / 2)

  def solve1(self):
    return self.solve(1)

  def solve2(self):
    return self.solve(2)
