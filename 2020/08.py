#!/usr/bin/env python3

from copy import deepcopy
from lib.solver import BaseSolver
from typing import Union

class Solver(BaseSolver):
  def calculate(self):
    self.items = list(map(lambda x: {"ops": x.split()[0], "arg": int(x.split()[1])}, self.input.splitlines()))

  def run(self, operations: list, calculate: bool = False) -> Union[int, bool]:
    ops_executed = []
    accumulator = 0
    i = 0

    while i not in ops_executed and i < len(self.items):
      ops_executed.append(i)
      jmp = 1
      if operations[i]["ops"] == b"acc" and calculate:
        accumulator += operations[i]["arg"]
      if operations[i]["ops"] == b"jmp":
        jmp = operations[i]["arg"]
      i += jmp

    if calculate:
      return accumulator

    return i == len(operations)

  def solve1(self):
    self.calculate()
    return self.run(self.items, True)

  def solve2(self):
    self.calculate()
    for k, i in enumerate(self.items):
      if i["ops"] == b"jmp":
        variant = deepcopy(self.items)
        variant[k]["ops"] = b"nop"
        if self.run(variant):
          return self.run(variant, True)
      elif i["ops"] == b"nop":
        variant = deepcopy(self.items)
        variant[k]["ops"] = b"jmp"
        if self.run(variant):
          return self.run(variant, True)
