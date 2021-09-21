import subprocess
import mutils
from typing import *

def solve_file(problem: str) -> mutils.PartialSolution:
  if problem[-1] != "\n":
    problem += "\n"
  t = subprocess.run(mutils.kissat_path, capture_output=True, input=problem, text=True)
  if t.stderr != "":
    raise mutils.KissatError(t.stderr)
  if "s UNSATISFIABLE" in t.stdout:
    return False
  out = t.stdout.splitlines()
  values = []
  for i in out:
    if i[0] == "v":
      j = i.split(" ")[1:]
      for k in j:
        values.append(int(k))
  return values[:-1]

def solve_clauses(problem: Sequence[mutils.Clause], n_vars: int) -> mutils.PartialSolution:
  file = f"p cnf {n_vars} {len(problem)}\n"
  for i in problem:
    for j in i:
      file += str(j) + " "
    file += "0\n"
  return solve_file(file)

def all_solutions(problem: list):
  ...

# testing to make sure I'm using kissat properly
if __name__ == "__main__":
  import sys
  print(solve_file(sys.argv[1].replace("l", "\n")))
