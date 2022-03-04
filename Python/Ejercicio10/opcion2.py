import os

def esPrimo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

inp = input("""
Inserta un número natural:
""")

i = int(inp) + 1
while not esPrimo(i):
    i += 1
print(i)

os.system(f"python menu.py")
raise SystemExit(0)
