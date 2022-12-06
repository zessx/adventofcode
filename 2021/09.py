#!/usr/bin/env python3

from lib.solver import BaseSolver
from math import prod

class Solver(BaseSolver):
  def calculate(self):
    self.items = [[int(i) for i in line.decode("utf-8")] for line in self.input.splitlines()]
    self.lowest_points = [item for sublist in [[[x,y] for y, i in enumerate(line) if self.is_lower_point(x, y)] for x, line in enumerate(self.items)] for item in sublist]

  def is_lower_point(self, x: int, y: int) -> bool:
    if x > 0 and self.items[x - 1][y] <= self.items[x][y]:
      return False
    if x < (len(self.items) - 1) and self.items[x + 1][y] <= self.items[x][y]:
      return False
    if y > 0 and self.items[x][y - 1] <= self.items[x][y]:
      return False
    if y < (len(self.items[x]) - 1) and self.items[x][y + 1] <= self.items[x][y]:
      return False
    return True

  def get_basin_size(self, x: int, y: int) -> int:
    basin = [[x, y]]
    previous_length = 0
    while len(basin) > previous_length:
      previous_length = len(basin)
      for i in basin:
        _x, _y = i
        if _x > 0 and [_x - 1, _y] not in basin and 9 > self.items[_x - 1][_y] > self.items[_x][_y]:
          basin.append([_x - 1, _y])
        if _x < (len(self.items) - 1) and [_x + 1, _y] not in basin and 9 > self.items[_x + 1][_y] > self.items[_x][_y]:
          basin.append([_x + 1, _y])
        if _y > 0 and [_x, _y - 1] not in basin and 9 > self.items[_x][_y - 1] > self.items[_x][_y]:
          basin.append([_x, _y - 1])
        if _y < (len(self.items[_x]) - 1) and [_x, _y + 1] not in basin and 9 > self.items[_x][_y + 1] > self.items[_x][_y]:
          basin.append([_x, _y + 1])
    return len(basin)

  def solve1(self):
    self.calculate()
    return sum([self.items[i[0]][i[1]] + 1 for i in self.lowest_points])

  def solve2(self):
    self.calculate()
    return prod(sorted([self.get_basin_size(*i) for i in self.lowest_points], reverse = True)[:3])
