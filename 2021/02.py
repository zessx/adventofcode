#!/usr/bin/env python3

from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self):
    self.items = self.input.splitlines()

  def solve1(self):
    self.calculate()

    s = lambda x: sum([int(i.split()[1]) for i in self.items if i.split()[0] == x])
    return s(b"forward") * (s(b"down") - s(b"up"))

  def solve2(self):
    self.calculate()

    posx = 0
    depth = 0
    aim = 0
    for i in self.items:
      action, amount = i.split()
      if action == b"forward":
        posx += int(amount)
        depth += int(amount) * aim
      elif action == b"down":
        aim += int(amount)
      elif action == b"up":
        aim -= int(amount)
    return posx * depth
