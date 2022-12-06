#!/usr/bin/env python3

import os
import requests
from typing import Mapping

def get_cookies() -> Mapping:
  return {
    "session": os.environ["AOC_SESSION_ID"]}

def get_input(year: int, day: int) -> str:
  request = requests.get(
    url = f"https://adventofcode.com/{str(year)}/day/{str(day)}/input",
    cookies = get_cookies())
  return request.content
