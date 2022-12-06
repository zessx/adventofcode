#!/usr/bin/env python3

import networkx as nx
from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self):
    self.items = [[int(x) for x in y] for y in self.input.decode("utf-8").splitlines()]

  def get_path_weight(self, items) -> None:
    h = len(items)
    w = len(items[0])
    g = nx.DiGraph()

    g.add_node(-1)
    g.add_edge(-1, 0, weight = items[0][0])

    for y, line in enumerate(items):
      for x, cell in enumerate(line):
        g.add_node(y * w + x)
        if x > 0:
          g.add_edge(y * w + x - 1, y * w + x, weight = cell)
        if y > 0:
          g.add_edge((y - 1) * w + x, y * w + x, weight = cell)

    path = nx.shortest_path(g, source = -1, target = w * h - 1, weight = "weight")
    return sum(items[int(c / w)][c % w] for c in path[2:])

  def solve1(self):
    self.calculate()
    return self.get_path_weight(self.items)
