#!/usr/bin/env python3

from functools import reduce
from lib.solver import BaseSolver
from math import floor

class Solver(BaseSolver):
  def calculate(self):
    self.items = self.input.splitlines()

    syntax_error_score_map = {
      ")": 3,
      "]": 57,
      "}": 1197,
      ">": 25137
    }
    incomplete_score_map = {
      ")": 1,
      "]": 2,
      "}": 3,
      ">": 4
    }

    self.syntax_errors_score = 0
    self.incomplete_scores = []
    for line in self.items:
      expected = []
      syntax_error = False
      for c in line.decode():
        if c == '[':
          expected.insert(0, ']')
        elif c == '<':
          expected.insert(0, '>')
        elif c == '(':
          expected.insert(0, ')')
        elif c == '{':
          expected.insert(0, '}')
        elif c == expected[0]:
          del expected[0]
        else:
          syntax_error = True
          self.syntax_errors_score += syntax_error_score_map[c]
          break
      if not syntax_error:
        chars_score = [incomplete_score_map[closer] for closer in expected]
        self.incomplete_scores.append(reduce(lambda a, b: a * 5 + b, chars_score))

    self.incomplete_scores.sort()

  def solve1(self):
    self.calculate()
    return self.syntax_errors_score

  def solve2(self):
    self.calculate()
    return self.incomplete_scores[floor(len(self.incomplete_scores) / 2)]
