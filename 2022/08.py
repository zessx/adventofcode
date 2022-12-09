#!/usr/bin/env python3

from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self):
    self.trees = [[char - 48 for char in line] for line in self.input.splitlines()]

  def is_visible(self, coords) -> bool:
    x, y = coords
    if x in [0, len(self.trees[0]) - 1] or y in [0, len(self.trees) - 1]:
      return True
    if max([tree for tree in self.trees[y][:x]]) < self.trees[y][x]:
      return True
    if max([tree for tree in self.trees[y][x+1:]]) < self.trees[y][x]:
      return True
    if max([tree for tree in [self.trees[_y][x] for _y in range(0, y)]]) < self.trees[y][x]:
      return True
    if max([tree for tree in [self.trees[_y][x] for _y in range(y+1, len(self.trees))]]) < self.trees[y][x]:
      return True
    return False

  def visibility_score(self, coords) -> bool:
    x, y = coords
    visible_score = 1
    visible_trees = 0
    for _x in range(x - 1, -1, -1):
      visible_trees += 1
      if self.trees[y][_x] >= self.trees[y][x]:
        break
    if visible_trees > 0:
      visible_score *= visible_trees
    visible_trees = 0
    for _x in range(x + 1, len(self.trees[y])):
      visible_trees += 1
      if self.trees[y][_x] >= self.trees[y][x]:
        break
    if visible_trees > 0:
      visible_score *= visible_trees
    visible_trees = 0
    for _y in range(y - 1, -1, -1):
      visible_trees += 1
      if self.trees[_y][x] >= self.trees[y][x]:
        break
    if visible_trees > 0:
      visible_score *= visible_trees
    visible_trees = 0
    for _y in range(y + 1, len(self.trees)):
      visible_trees += 1
      if self.trees[_y][x] >= self.trees[y][x]:
        break
    if visible_trees > 0:
      visible_score *= visible_trees
    return visible_score

  def solve1(self):
    self.calculate()
    return sum([
      1
      for y in range(len(self.trees)) for x in range(len(self.trees[y]))
      if self.is_visible((x, y))])

  def solve2(self):
    self.calculate()
    return max([
      self.visibility_score((x, y))
      for y in range(len(self.trees)) for x in range(len(self.trees[y]))])
