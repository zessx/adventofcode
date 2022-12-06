#!/usr/bin/env python3

import re
from lib.solver import BaseSolver

class Solver(BaseSolver):
  def solve1(self):
    def check_policy(line: bytes) -> bool:
      m = re.match(rb"^(?P<min>\d+)-(?P<max>\d+)\s(?P<letter>[a-z]):\s(?P<password>[a-z]+)$", line).groupdict()
      return int(m["min"]) <= m["password"].count(m["letter"]) <= int(m["max"])

    return len([line for line in self.input.splitlines() if check_policy(line)])

  def solve2(self):
    def check_policy(line: bytes) -> bool:
      m = re.match(rb"^(?P<i1>\d+)-(?P<i2>\d+)\s(?P<letter>[a-z]):\s(?P<password>[a-z]+)$", line).groupdict()
      return int(str.encode(chr(m["password"][int(m["i1"]) - 1])) == m["letter"]) \
        + int(str.encode(chr(m["password"][int(m["i2"]) - 1])) == m["letter"]) == 1

    return len([line for line in self.input.splitlines() if check_policy(line)])

