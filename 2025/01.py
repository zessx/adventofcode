#!/usr/bin/env python3

from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self):
    current = 50
    self.zero_stop_counter = 0
    self.zero_click_counter = 0

    for line in self.input.splitlines():
      shift = int(line[1:])

      previous = current
      current += ((shift % 100) * (1 if chr(line[0]) == 'L' else -1))
      self.zero_click_counter += shift // 100

      if current % 100 == 0:
        self.zero_stop_counter += 1
        self.zero_click_counter += 1
      elif current < 0 and previous != 0:
          self.zero_click_counter += 1
      elif current > 100:
        self.zero_click_counter += 1

      current %= 100

  def solve1(self):
    self.calculate()
    return self.zero_stop_counter

  def solve2(self):
    self.calculate()
    return self.zero_click_counter
