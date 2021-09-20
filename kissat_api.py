import subprocess
import os
import copy

def warn(msg=None):
  if msg is None:
    print("\033[31mWARNING\033[0m")
  else:
    print("\033[31mWARNING: " + msg + "\033[0m")

KISSAT_PATH = "./kissat.exe"

if not os.path.exists(KISSAT_PATH): # try to build kissat if possible
  warn("kissat executable not found")
  os.chdir("kissat")
  proc = subprocess.run(["sh", "build.sh"])
  os.chdir("..")
  if proc.returncode != 0:
    exit(1)
  else:
    print("\033[32mkissat build successful\033[0m")

class CNF_Problem:
  def __init__(self, file="input.cnf"):
    self.num_vars = 0
    self.num_clauses = 0
    self.vars = []
    self.map = {}
    self.clauses = ""
  
  def add_clause(self, cls):
    if type(cls) == list:
      cls = " ".join(cls)
    vars = cls.replace("-", "").split(" ")
    for i in vars:
      if i in self.vars:
        cls = cls.replace(i, str(self.map[i]))
      else:
        self.num_vars += 1
        self.vars.append(i)
        self.map.update({i: self.num_vars})
        cls = cls.replace(i, str(self.num_vars))
    self.clauses += cls + " 0\n"
  
  def solve(self):
    with open(self.file, "w") as f:
      f.write(f"p cnf {self.num_vars} {self.num_clauses}\n")
      f.write(self.clauses)
    output = subprocess.run([KISSAT_PATH, self.file], capture_output=True, text=True).stdout
    if "s UNSATISFIABLE" in output:
      return False
    raw = ""
    for i in output.splitlines():
      if i[0] == "v":
        raw += i
    raw = raw.replace("v", "")[1:-2]
    raw = [int(i) for i in raw.split(" ")]
    sol = {}
    for i in range(self.num_vars):
      sol.update({self.vars[i]: int(raw[i] > 0)})
    return sol
  
  def without(self, sol):
    clause = []
    for i in sol:
      if sol[i] == 0:
        ind = 
  
  def find_all_solutions(self):
    sols = []
    while True:
      s = self.solve()
      if s == False:
        return sols
      sols.append(s)

