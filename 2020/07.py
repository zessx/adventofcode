#!/usr/bin/env python3

import re
from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self):
    self.rules = {}
    for rule in self.input.splitlines():
      key = re.match(rb"^(?P<key>\w+\s\w+) bags contain", rule).groupdict()["key"]
      values = re.findall(rb".(?P<amount>\d+) (?P<type>\w+\s\w+) bags?", rule)
      self.rules[key] = {}
      for amount, type in values:
        self.rules[key][type] = int(amount)

  def bags_can_contains(self, bag) -> set:
    bags = set([key for key, value in self.rules.items() if bag in value.keys()])
    for key in bags.copy():
      bags.update(self.bags_can_contains(key))
    return bags

  def bag_contains(self, bag) -> int:
    return sum([value + value * self.bag_contains(key) for key, value in self.rules[bag].items()])

  def solve1(self):
    self.calculate()
    return len(self.bags_can_contains(b"shiny gold"))

  def solve2(self):
    self.calculate()
    return self.bag_contains(b"shiny gold")
