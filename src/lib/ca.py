import mutils
from typing import *

N_HOODS = 'cekainyqjrtwz'
NAPKINS = {
  k: dict(zip(N_HOODS, v)) for k, v in {
    '0': '',
    '1': ['00000001', '10000000'],
    '2': ['01000001', '10000010', '00100001', '10000001', '10001000', '00010001'],
    '3': ['01000101', '10100010', '00101001', '10000011', '11000001', '01100001', '01001001', '10010001', '10100001', '10001001'],
    '4': ['01010101', '10101010', '01001011', '11100001', '01100011', '11000101', '01100101', '10010011', '10101001', '10100011', '11001001', '10110001', '10011001'],
    '5': ['10111010', '01011101', '11010110', '01111100', '00111110', '10011110', '10110110', '01101110', '01011110', '01110110'],
    '6': ['10111110', '01111101', '11011110', '01111110', '01110111', '11101110'],
    '7': ['11111110', '01111111'],
    '8': ''
  }.items()
}

def parse_transition(s: str) -> Sequence[str]:
  if s == "":
    return []
  elif s in ["0", "8"]:
    return [s]
  elif len(s) == 1: # all transitions
    return [s + i for i in NAPKINS[s]]
  elif "-" in s: # excluded transitions case
    t = list(NAPKINS[s].keys())
    for i in s[2:]:
      t.remove(i)
    return [s[0] + i for i in t]
  else: # positive transitions
    return [s[0] + i for i in s[1:]]

def parse_conditions(s: str) -> Sequence[str]:
  s = mutils.replacedict(s, {
    "B": "",
    "S": "",
    "0": "|0",
    "1": "|1",
    "2": "|2",
    "3": "|3",
    "4": "|4",
    "5": "|5",
    "6": "|6",
    "7": "|7",
    "8": "8"
  }).split("|")
  transitions = []
  for i in s:
    transitions += parse_transition(i)
  return transitions

def parse_hensel(s: str) -> Tuple[Sequence[str], Sequence[str]]:
  s = s.split("/")
  return (parse_conditions(s[0]), parse_conditions(s[1]))
