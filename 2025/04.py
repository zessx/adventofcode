#!/usr/bin/env python3

from lib.solver import BaseSolver

class Solver(BaseSolver):
  def find_removable_rolls(self, graph):
    return [roll for roll, neighbors in graph.items() if len(neighbors) < 4]

  def calculate(self):
    self.graph = {}
    for y, line in enumerate(self.input.splitlines()):
      for x, char in enumerate(line):
        if char == ord(b'@'):
          neighbors = []
          for dx, dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(line) and 0 <= ny < len(self.input.splitlines()):
              if self.input.splitlines()[ny][nx] == ord(b'@'):
                neighbors.append((nx, ny))
          self.graph[(x, y)] = neighbors

  def solve1(self):
    self.calculate()
    return len(self.find_removable_rolls(self.graph))

  def solve2(self):
    self.calculate()

    removed_rolls = []
    graph = self.graph.copy()
    while True:
      removable_rolls = self.find_removable_rolls(graph)
      if len(removable_rolls) == 0:
        break
      removed_rolls.extend(removable_rolls)
      for roll in removable_rolls:
        del graph[(roll[0], roll[1])]
        for n in graph:
          graph[n] = [x for x in graph[n] if x != roll]

    return len(removed_rolls)

