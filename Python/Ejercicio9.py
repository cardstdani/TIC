import numpy as np
inp = int(input("Introduce un número: "))

l = []
for i in range(1, inp+1):
  nl = [i + (a*i) for a in range(inp)]
  l.append(nl + [sum(nl)])

print(np.matrix(l))
