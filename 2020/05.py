#!/usr/bin/env python3

from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self):
    self.seat_ids = [self.get_id(item) for item in self.input.splitlines()]

  def get_id(self, boarding_pass: bytes) -> int:
    binary_rep = boarding_pass \
      .replace(b"F", b"0") \
      .replace(b"B", b"1") \
      .replace(b"R", b"1") \
      .replace(b"L", b"0")
    return int(binary_rep[:7], 2) * 8 + int(binary_rep[7:], 2)

  def solve1(self):
    self.calculate()
    return max(self.seat_ids)

  def solve2(self):
    self.calculate()
    seats_with_empty_front = [item - 1 for item in self.seat_ids if item - 1 not in self.seat_ids]
    seats_with_empty_back = [item + 1 for item in self.seat_ids if item + 1 not in self.seat_ids]
    return list(set(seats_with_empty_front).intersection(seats_with_empty_back))[0]
