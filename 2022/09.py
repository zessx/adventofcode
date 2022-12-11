#!/usr/bin/env python3

from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self, length: int):
    self.moves = [move.split(b' ') for move in self.input.splitlines()]

    self.history = [[(0, 0)] * length]

    for move in self.moves:
      direction, amount = move
      for _ in range(int(amount)):
        new_position = []
        for i in range(length):
          current = list(self.history[-1][i])
          if i == 0:
            if direction == b'U':
              current[1] -= 1
            elif direction == b'D':
              current[1] += 1
            elif direction == b'R':
              current[0] += 1
            elif direction == b'L':
              current[0] -= 1
          else:
            previous = list(new_position[-1])
            if previous[1] == current[1] + 2:
              current[0] += \
                (previous[0] - current[0]) \
                if abs((previous[0] - current[0])) < 2 \
                else (previous[0] - current[0]) / abs((previous[0] - current[0]))
              current[1] += 1
            elif previous[1] == current[1] - 2:
              current[0] += \
                (previous[0] - current[0]) \
                if abs((previous[0] - current[0])) < 2 \
                else (previous[0] - current[0]) / abs((previous[0] - current[0]))
              current[1] -= 1
            elif previous[0] == current[0] + 2:
              current[0] += 1
              current[1] += \
                (previous[1] - current[1]) \
                if abs((previous[1] - current[1])) < 2 \
                else (previous[1] - current[1]) / abs((previous[1] - current[1]))
            elif previous[0] == current[0] - 2:
              current[0] -= 1
              current[1] += \
                (previous[1] - current[1]) \
                if abs((previous[1] - current[1])) < 2 \
                else (previous[1] - current[1]) / abs((previous[1] - current[1]))
          new_position.append(tuple(current))
        self.history.append(new_position)

  def solve1(self):
    self.calculate(length = 2)
    return len(set([position[-1] for position in self.history]))

  def solve2(self):
    self.calculate(length = 10)
    return len(set([position[-1] for position in self.history]))
