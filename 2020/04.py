#!/usr/bin/env python3

import re
from lib.solver import BaseSolver
from typing import Dict

class Solver(BaseSolver):
  def calculate(self):
    self.passports = []
    current_passport = {}
    for line in self.input.splitlines():
      if line == b"":
        self.passports.append(current_passport)
        current_passport = {}
      else:
        for field in line.split():
          key, value = field.split(b":")
          current_passport[key] = value
    self.passports.append(current_passport)

  def solve1(self):
    self.calculate()

    def is_passport_valid(passport: Dict) -> bool:
      return len(passport) == 8 or (len(passport) == 7 and b"cid" not in passport)

    return len([p for p in self.passports if is_passport_valid(p)])

  def solve2(self):
    self.calculate()

    def is_passport_valid(passport: Dict) -> bool:
      return (len(passport) == 8 or (len(passport) == 7 and b"cid" not in passport)) and \
        re.match(rb"^\d{4}$", passport[b"byr"]) and 1920 <= int(passport[b"byr"]) <= 2002 and \
        re.match(rb"^\d{4}$", passport[b"iyr"]) and 2010 <= int(passport[b"iyr"]) <= 2020 and \
        re.match(rb"^\d{4}$", passport[b"eyr"]) and 2020 <= int(passport[b"eyr"]) <= 2030 and \
        ( \
          (re.match(rb"^\d+cm$", passport[b"hgt"]) and 150 <= int(passport[b"hgt"][:-2]) <= 193) or \
          (re.match(rb"^\d+in$", passport[b"hgt"]) and 59 <= int(passport[b"hgt"][:-2]) <= 76) \
        ) and \
        re.match(rb"^\#[0-9a-f]{6}$", passport[b"hcl"]) and \
        passport[b"ecl"] in (b"amb", b"blu", b"brn", b"gry", b"grn", b"hzl", b"oth") and \
        re.match(rb"^\d{9}$", passport[b"pid"])

    return len([p for p in self.passports if is_passport_valid(p)])
