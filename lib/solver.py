#!/usr/bin/env python3

from lib.http import get_input

class BaseSolver():
  input: str

  def __init__(self, year: int, day: int):
    self.input = get_input(year, day)

  def solve1(self):
    raise NotImplementedError("Method solve1 not implemented")

  def solve2(self):
    raise NotImplementedError("Method solve2 not implemented")
