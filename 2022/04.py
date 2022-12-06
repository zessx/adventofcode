#!/usr/bin/env python3

from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self):
    self.assignments = [
      [sections.split(b'-') for sections in assignment.split(b',')]
      for assignment in self.input.splitlines()]

  def solve1(self):
    self.calculate()
    return len([
      assignment
      for assignment in self.assignments
      if (int(assignment[0][0]) >= int(assignment[1][0]) and int(assignment[0][1]) <= int(assignment[1][1]))
      or (int(assignment[1][0]) >= int(assignment[0][0]) and int(assignment[1][1]) <= int(assignment[0][1]))])

  def solve2(self):
    self.calculate()
    return len([
      assignment
      for assignment in self.assignments
      if len(list(
          set(range(int(assignment[0][0]), int(assignment[0][1]) + 1))
        & set(range(int(assignment[1][0]), int(assignment[1][1]) + 1))))])

