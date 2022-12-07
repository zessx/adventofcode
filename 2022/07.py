#!/usr/bin/env python3

from lib.solver import BaseSolver

class Solver(BaseSolver):
  def calculate(self):
    self.tree = {
      b"/": {
        "type": "dir",
        "size": 0
      }
    }

    current_path = []
    for line in self.input.splitlines():
      args = line.split(b' ')
      if args[0] == b"$":
        if args[1] == b"cd":
          if args[2] == b"/":
            current_path = []
          elif args[2] == b"..":
            current_path = current_path[:-1]
          else:
            current_path.append(args[2])
            path = b"/" + b"/".join(current_path)
            if path not in self.tree:
              self.tree[path] = {
                "type": "dir",
                "size": 0
              }
      else:
        if args[0] == b"dir":
          path = b"/" + b"/".join(current_path + [args[1]])
          if path not in self.tree:
            self.tree[path] = {
              "type": "dir",
              "size": 0
            }
        else:
          path = b"/" + b"/".join(current_path + [args[1]])
          if path not in self.tree:
            self.tree[path] = {
              "type": "file",
              "size": int(args[0])
            }
          parents = current_path.copy()
          while len(parents):
            path = b"/" + b"/".join(parents)
            self.tree[path]["size"] += int(args[0])
            parents.pop()
          self.tree[b"/"]["size"] += int(args[0])

  def solve1(self):
    self.calculate()
    return sum([item['size']
      for _, item in self.tree.items()
      if item['type'] == 'dir' and item['size'] <= 100000])

  def solve2(self):
    self.calculate()
    min_dir_size = 30000000 - (70000000 - self.tree[b"/"]["size"])
    return min([item['size']
      for _, item in self.tree.items()
      if item['type'] == 'dir' and item['size'] >= min_dir_size])
