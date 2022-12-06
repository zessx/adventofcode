#!/usr/bin/env python3

from itertools import chain
from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self):
    self.items = [[int(chr(c)) for c in l] for l in self.input.splitlines()]

  def solve(self, solve_step: int):
    self.calculate()

    flashes = 0
    step = 0
    items = self.items.copy()

    while True:
      step += 1
      new_items = items.copy()
      flashed = []

      for kl, line in enumerate(self.items):
        flashed_line = []
        for kc, _ in enumerate(line):
          new_items[kl][kc] += 1
          flashed_line.append(False)
        flashed.append(flashed_line)

      while True:
        flashable = list(chain.from_iterable([[[kl, kc] for kc, char in enumerate(line) if char > 9 and not flashed[kl][kc]] for kl, line in enumerate(new_items)]))
        if len(flashable) == 0:
          break

        for x, y in flashable:
          flashed[x][y] = True
          flashes += 1
          if y > 0:
            new_items[x][y - 1] += 1
          if y < len(new_items[x]) - 1:
            new_items[x][y + 1] += 1
          if x > 0:
            new_items[x - 1][y] += 1
            if y > 0:
              new_items[x - 1][y - 1] += 1
            if y < len(new_items[x - 1]) - 1:
              new_items[x - 1][y + 1] += 1
          if x < len(new_items) - 1:
            new_items[x + 1][y] += 1
            if y > 0:
              new_items[x + 1][y - 1] += 1
            if y < len(new_items[x + 1]) - 1:
              new_items[x + 1][y + 1] += 1

      count_flashed = 0
      for kl, line in enumerate(flashed):
        for kc, has_flashed in enumerate(line):
          if has_flashed:
            new_items[kl][kc] = 0
            count_flashed += 1

      items = new_items.copy()

      if solve_step == 1 and step == 100:
        return flashes

      if solve_step == 2 and count_flashed == len(new_items) * len(new_items[0]):
        return step

  def solve1(self):
    return self.solve(1)

  def solve2(self):
    return self.solve(2)
