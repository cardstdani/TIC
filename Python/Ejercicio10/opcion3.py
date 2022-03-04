import os

def esPrimo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

inp = int(input("""
Inserta un número natural:
"""))

n = 0
for i in range(2, inp):
    if esPrimo(i):
        n += 1
print(n)

os.system(f"python menu.py")
raise SystemExit(0)
