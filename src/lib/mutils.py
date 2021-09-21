from typing import *
import os.path

# types
Clause = Sequence[int]
Solution = Sequence[int]
PartialSolution = Union[Solution, Literal[False]]
class KissatError(Exception):
  ...

def replacedict(s: str, d: Mapping[str, str]) -> str:
  for pattern, replacement in d.items():
    s = s.replace(pattern, replacement)
  return s

def clause_negation(clause: Clause) -> Clause:
  return [-i for i in clause]

kissat_path = ""
candidates = ["./kissat.exe", "./lib/kissat.exe", "./src/lib/kissat.exe", "../kissat.exe"] # will be called from various places so need to test various possibilities
for i in candidates:
  if os.path.exists(i):
    kissat_path = os.path.abspath(i)
