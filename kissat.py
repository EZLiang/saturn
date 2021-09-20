import subprocess

class KissatError(Exception):
  ...

def solve(problem):
  if problem[-1] != "\n":
    problem += "\n"
  t = subprocess.run("./kissat.exe", capture_output=True, input=problem, text=True)
  if t.stderr != "":
    raise KissatError(t.stderr)
  if "s UNSATISFIABLE" in t.stdout:
    return False
  out = t.stdout.splitlines()
  values = []
  for i in out:
    if i[0] == "v":
      j = i.split(" ")[1:]
      for k in j:
        values.append(int(k))
  return values

if __name__ == "__main__":
  import sys
  print(solve(sys.argv[1].replace("l", "\n")))
