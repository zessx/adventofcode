#!/usr/bin/env python3

import re
from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self):
    self.stacks_9000 = []
    self.stacks_9001 = []
    for line in self.input.splitlines():
      if line[:3] == b' 1 ':
        for _ in range(len(line.strip().split(b'   '))):
          self.stacks_9000.append([])
          self.stacks_9001.append([])
        break

    for line in self.input.splitlines():
      if line:
        if line.strip()[0] == 91:
          for i in range(0, len(line), 4):
            if line[i + 1] != 32:
              self.stacks_9000[int(i / 4)] = [line[i + 1]] + self.stacks_9000[int(i / 4)]
              self.stacks_9001[int(i / 4)] = [line[i + 1]] + self.stacks_9001[int(i / 4)]

        if line[:4] == b'move':
          matches = re.match(rb'move (?P<amount>\d+) from (?P<from>\d+) to (?P<to>\d+)', line)

          for i in range(int(matches['amount'])):
            crate = self.stacks_9000[int(matches['from']) - 1].pop()
            self.stacks_9000[int(matches['to']) - 1].append(crate)

          self.stacks_9001[int(matches['to']) - 1].extend(self.stacks_9001[int(matches['from']) - 1][- int(matches['amount']):])
          self.stacks_9001[int(matches['from']) - 1] = self.stacks_9001[int(matches['from']) - 1][:- int(matches['amount'])]

  def solve1(self):
    self.calculate()
    return ''.join([chr(stack[-1]) if len(stack) else ' ' for stack in self.stacks_9000])

  def solve2(self):
    self.calculate()
    return ''.join([chr(stack[-1]) if len(stack) else ' ' for stack in self.stacks_9001])
