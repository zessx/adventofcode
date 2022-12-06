#!/usr/bin/env python3

from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self):
    self.items = self.input.splitlines()

  def solve(self, solve_step: int):
    self.calculate()

    numbers = self.items[0].split(b",")
    cardboards = []

    current_cardboard = []
    for i in self.items[2:]:
      if i == b"":
        cardboards.append(current_cardboard)
        current_cardboard = []
      else:
        current_cardboard.append(dict.fromkeys(i.strip().split(), False))
    cardboards.append(current_cardboard)

    def check_lines(cardboard) -> bool:
      return len([line for line in cardboard if False not in line.values()]) > 0

    def check_columns(carboard) -> bool:
      return len([column for column in [[line[list(line.keys())[c]] for line in carboard] for c in range(5)] if False not in column]) > 0

    winner_found = False
    loser_found = False
    last_cardboard = None
    for n in numbers:
      cardboards = [[({**line, **{n: True}} if n in line.keys() else line) for line in cardboard] for cardboard in cardboards]
      winning_cardboards = [cardboard for cardboard in cardboards if check_lines(cardboard) or check_columns(cardboard)]
      remaining_cardboards_indices = [k for k, cardboard in enumerate(cardboards) if not(check_lines(cardboard) or check_columns(cardboard))]
      if len(winning_cardboards) > 0 and not winner_found:
        if solve_step == 1:
          return sum([sum([int(k) for k, v in line.items() if not v]) for line in winning_cardboards[0]]) * int(n)
        winner_found = True
      if len(winning_cardboards) == len(cardboards) and not loser_found:
        if solve_step == 2:
          return sum([sum([int(k) for k, v in line.items() if not v]) for line in cardboards[last_cardboard]]) * int(n)
        loser_found = True
      if len(remaining_cardboards_indices) == 1 and last_cardboard == None:
        last_cardboard = remaining_cardboards_indices[0]

  def solve1(self):
    return self.solve(1)

  def solve2(self):
    return self.solve(2)
