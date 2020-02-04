f = open("benchmarks/.gitkeep", "r")
num = 0
r = f.read()
if r.isdigit():
  num = int(r) + 1

f = open("benchmarks/.gitkeep", "a")
f.write(str(num))
f.close()