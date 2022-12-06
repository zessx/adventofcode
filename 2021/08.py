#!/usr/bin/env python3

from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self):
    self.items = [
      {
        "signal": i.split("|")[0].strip(),
        "output": i.split("|")[1].strip()}
      for i in self.input.decode("utf-8").splitlines()]

  def solve1(self):
    self.calculate()
    return sum([len([digit for digit in item["output"].split() if len(digit) in [2, 3, 4, 7]]) for item in self.items])

  def solve2(self):
    self.calculate()

    outputs = []
    for item in self.items:
      m = {}
      m["a"] = ["a", "b", "c", "d", "e", "f", "g"]
      m["b"] = ["a", "b", "c", "d", "e", "f", "g"]
      m["c"] = ["a", "b", "c", "d", "e", "f", "g"]
      m["d"] = ["a", "b", "c", "d", "e", "f", "g"]
      m["e"] = ["a", "b", "c", "d", "e", "f", "g"]
      m["f"] = ["a", "b", "c", "d", "e", "f", "g"]
      m["g"] = ["a", "b", "c", "d", "e", "f", "g"]

      # 1 -> (cf)
      digits_1 = [digit for digit in item["signal"].split() if len(digit) == 2]
      chars = [c for c in digits_1[0]]
      m["c"] = [c for c in m["c"] if c in chars]
      m["f"] = [c for c in m["f"] if c in chars]

      # 7 -> a (cf)
      digits_7 = [digit for digit in item["signal"].split() if len(digit) == 3]
      chars = [c for c in digits_7[0]]
      m["a"] = [c for c in m["a"] if c in chars and c not in m["c"]]
      for d in range(ord("b"), ord("g") + 1):
        m[chr(d)] = [c for c in m[chr(d)] if c not in m["a"]]

      # 4 -> a (cf) (bd)
      digits_4 = [digit for digit in item["signal"].split() if len(digit) == 4]
      chars = [c for c in digits_4[0]]
      m["b"] = [c for c in m["b"] if c in chars and c not in m["c"]]
      m["d"] = [c for c in m["d"] if c in chars and c not in m["c"]]

      # 9 -> a g (cf) (bd)
      digits_9 = [digit for digit in item["signal"].split() if len(digit) == 6 \
        and m["a"][0] in digit \
        and m["b"][0] in digit \
        and m["b"][1] in digit \
        and m["c"][0] in digit \
        and m["c"][1] in digit \
        and m["d"][0] in digit \
        and m["d"][1] in digit \
        and m["f"][0] in digit \
        and m["f"][1] in digit]
      chars = [c for c in digits_9[0]]
      m["g"] = [c for c in m["g"] if c in chars \
        and c not in m["a"] \
        and c not in m["b"] \
        and c not in m["c"]]
      for d in range(ord("a"), ord("f") + 1):
        m[chr(d)] = [c for c in m[chr(d)] if c not in m["g"]]

      # 8 -> a e g (cf) (bd)
      m["e"] = [c for c in m["e"] if \
        c not in m["a"] \
        and c not in m["b"] \
        and c not in m["c"] \
        and c not in m["d"] \
        and c not in m["f"] \
        and c not in m["g"]]
      for d in range(ord("a"), ord("g") + 1):
        if chr(d) != "e":
          m[chr(d)] = [c for c in m[chr(d)] if c not in m["e"]]

      # 0 -> a b d e g (cf)
      digits_0 = [digit for digit in item["signal"].split() if len(digit) == 6 \
        if (m["b"][0] in digit and m["b"][1] not in digit) \
        or (m["b"][1] in digit and m["b"][0] not in digit)]
      chars = [c for c in digits_0[0]]
      m["b"] = [c for c in m["b"] if c in chars]
      m["d"] = [c for c in m["d"] if c not in chars]

      # 6 -> a b c d e f g
      digits_6 = [digit for digit in item["signal"].split() if len(digit) == 6 \
        if m["b"][0] in digit \
        and m["d"][0] in digit \
        and m["e"][0] in digit]
      chars = [c for c in digits_6[0]]
      m["f"] = [c for c in m["f"] if c in chars]
      m["c"] = [c for c in m["c"] if c not in chars]

      digits_map = {}
      digits_map[''.join(sorted(m["a"][0] + m["b"][0] + m["c"][0] + m["e"][0] + m["f"][0] + m["g"][0]))] = "0"
      digits_map[''.join(sorted(m["c"][0] + m["f"][0]))] = "1"
      digits_map[''.join(sorted(m["a"][0] + m["c"][0] + m["d"][0] + m["e"][0] + m["g"][0]))] = "2"
      digits_map[''.join(sorted(m["a"][0] + m["c"][0] + m["d"][0] + m["f"][0] + m["g"][0]))] = "3"
      digits_map[''.join(sorted(m["b"][0] + m["c"][0] + m["d"][0] + m["f"][0]))] = "4"
      digits_map[''.join(sorted(m["a"][0] + m["b"][0] + m["d"][0] + m["f"][0] + m["g"][0]))] = "5"
      digits_map[''.join(sorted(m["a"][0] + m["b"][0] + m["d"][0] + m["e"][0] + m["f"][0] + m["g"][0]))] = "6"
      digits_map[''.join(sorted(m["a"][0] + m["c"][0] + m["f"][0]))] = "7"
      digits_map["abcdefg"] = "8"
      digits_map[''.join(sorted(m["a"][0] + m["b"][0] + m["c"][0] + m["d"][0] + m["f"][0] + m["g"][0]))] = "9"

      outputs.append(int(''.join([digits_map[''.join(sorted(digit))] for digit in item["output"].split()])))

    return sum(outputs)
