#!/usr/bin/env python3

import argparse
import importlib
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def main():
  parser = argparse.ArgumentParser(description = "AdventOfCode Solver")
  parser.add_argument("--day", "-d", help = "Day of the challenge to solve (default, now)")
  parser.add_argument("--year", "-y", help = "Year of the challenge to solve (default, now)")

  args = parser.parse_args()

  day = datetime.now().day if args.day is None else int(args.day)
  year = datetime.now().year if args.year is None else int(args.year)

  try:
    lib = importlib.import_module(f'{year:04d}.{day:02d}')
    solver = lib.Solver(year, day)
    print(solver.solve1())
    print(solver.solve2())
  except ModuleNotFoundError:
    print(f'{year:04d}.{day:02d}: Solver not found')
  except NotImplementedError as e:
    print(f'{year:04d}.{day:02d}: {e}')

if __name__ == '__main__':
  main()
