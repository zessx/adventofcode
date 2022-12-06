#!/usr/bin/env python3

from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self):
    self.items = [l.decode("utf-8") for l in self.input.splitlines()]
    self.points = [[int(p) for p in i.split(",")] for i in self.items if "," in i]
    self.instructions = [i.replace("fold along ", "").split("=") for i in self.items if "fold" in i]

  def fold(self, points: list, axis: int, axis_type: str) -> list:
    new_points = [p for p in points if p[1] < axis]
    if axis_type == "y":
      new_points = [p for p in points if p[1] < axis]
      for point in points:
        if point[1] > axis:
          new_point = [point[0], point[1] - (point[1] - axis) * 2]
          if new_point not in new_points:
            new_points.append(new_point)
    else:
      new_points = [p for p in points if p[0] < axis]
      for point in points:
        if point[0] > axis:
          new_point = [point[0] - (point[0] - axis) * 2, point[1]]
          if new_point not in new_points:
            new_points.append(new_point)
    return new_points

  def solve1(self):
    self.calculate()

    return len(self.fold(self.points, int(self.instructions[0][1]), self.instructions[0]))

  def solve2(self):
    self.calculate()

    points = self.points.copy()
    for _, i in enumerate(self.instructions):
      points = self.fold(points, int(i[1]), i[0])

    w = max([p[0] for p in points])
    h = max([p[1] for p in points])

    output = ''
    for y in range(h + 1):
      for x in range(w + 1):
        output += '#' if [x, y] in points else ' '
      output += "\n"

    return output
