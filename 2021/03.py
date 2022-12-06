#!/usr/bin/env python3

from lib.solver import BaseSolver
from math import ceil

class Solver(BaseSolver):
  def calculate(self):
    self.items = self.input.splitlines()
    self.bit_length = len(self.items[0])

  def solve1(self):
    self.calculate()

    gamma_s = ""
    for b in range(self.bit_length):
      gamma_s += "1" if len([i for i in self.items if i[b] == ord("1")]) > (len(self.items) / 2) else "0"
    epsilon_s = "".join([str(int(not bool(int(i)))) for i in gamma_s])

    gamma = int(gamma_s, 2)
    epsilon = int(epsilon_s, 2)

    return gamma * epsilon

  def solve2(self):
    self.calculate()

    options_oxygen = self.items.copy()
    options_co2 = self.items.copy()
    oxygen_s = None
    co2_s = None
    for b in range(self.bit_length):
      if oxygen_s == None:
        bit_oxygen = "1" if len([i for i in options_oxygen if i[b] == ord("1")]) >= ceil(len(options_oxygen) / 2) else "0"
        options_oxygen = [i for i in options_oxygen if i[b] == ord(bit_oxygen)]
        if len(options_oxygen) == 1:
          oxygen_s = options_oxygen[0]
      if co2_s == None:
        bit_co2 = "1" if len([i for i in options_co2 if i[b] == ord("1")]) < ceil(len(options_co2) / 2) else "0"
        options_co2 = [i for i in options_co2 if i[b] == ord(bit_co2)]
        if len(options_co2) == 1:
          co2_s = options_co2[0]

    oxygen = int(oxygen_s, 2)
    co2 = int(co2_s, 2)

    return oxygen * co2
