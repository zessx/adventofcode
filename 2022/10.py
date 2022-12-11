#!/usr/bin/env python3

from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self):
    self.instructions = [bytes.decode(instruction, "utf8") for instruction in self.input.splitlines()]
    self.signals = []

    x = 1
    for instruction in self.instructions:
      self.signals.append(x)
      if instruction != "noop":
        _, shift = instruction.split(" ")
        x += int(shift)
        self.signals.append(x)

  def solve1(self):
    self.calculate()
    return sum([self.signals[i-2] * i for i in range(20, len(self.signals) + 1, 40)])

  def solve2(self):
    self.calculate()
    output = ['#' if self.signals[i-1] in range((i % 40) - 1, (i % 40) + 2) else '.' for i in range(len(self.signals))]
    return '\n'.join([''.join(output[i:i+40]) for i in range(0, len(output), 40)])
