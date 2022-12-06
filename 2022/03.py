#!/usr/bin/env python3

from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self):
    self.rucksacks = self.input.splitlines()

  def solve1(self):
    self.calculate()
    return sum([
      [(item - 38 if item <= 90 else item - 96)
        for item in rucksack[:int(len(rucksack) / 2)]
        if item in rucksack[int(len(rucksack) / 2):]][0]
      for rucksack in self.rucksacks])

  def solve2(self):
    self.calculate()
    return sum([
      [(item - 38 if item <= 90 else item - 96)
        for item in self.rucksacks[i]
        if item in self.rucksacks[i + 1] and item in self.rucksacks[i + 2]][0]
      for i in range(0, len(self.rucksacks), 3)])

