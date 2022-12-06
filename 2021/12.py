#!/usr/bin/env python3

import re
from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self):
    self.items = [l.decode("utf-8").split("-") for l in self.input.splitlines()]

  def solve1(self):
    self.calculate()

    unfinished_paths = [["start"]]
    paths = []
    while len(unfinished_paths) > 0:
      path = unfinished_paths.pop()
      next_caves = \
        [i[0] for i in self.items if i[1] == path[-1] and not (re.match(r"^[a-z]+$", i[0]) and i[0] in path)] + \
        [i[1] for i in self.items if i[0] == path[-1] and not (re.match(r"^[a-z]+$", i[1]) and i[1] in path)]
      for n in next_caves:
        if n == "end":
          paths.append(path + [n])
        else:
          unfinished_paths.append(path + [n])

    return len(paths)

  def solve2(self):
    self.calculate()

    unfinished_paths = [["start"]]
    paths = []
    while len(unfinished_paths) > 0:
      path = unfinished_paths.pop()
      small_double = [i for i in path if re.match(r"^[a-z]+$", i) and path.count(i) > 1]
      next_caves = \
        [i[0] for i in self.items if i[1] == path[-1] \
          and not (i[0] in ["start", "end"] and i[0] in path) \
          and not (re.match(r"^[a-z]+$", i[0]) and i[0] in path and len(small_double) > 0)] + \
        [i[1] for i in self.items if i[0] == path[-1] \
          and not (i[1] in ["start", "end"] and i[1] in path) \
          and not (re.match(r"^[a-z]+$", i[1]) and i[1] in path and len(small_double) > 0)]
      if path[1:5] == ['start', 'A', 'c', 'A']:
        print(str(path) + " -> " + str(next_caves))
      for n in next_caves:
        if n == "end":
          paths.append(path + [n])
        else:
          unfinished_paths.append(path + [n])

    return len(paths)
