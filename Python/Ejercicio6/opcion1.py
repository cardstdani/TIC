import os

def esPrimo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

inp = input("""
Inserta dos números naturales:
""").split()

for i in range(int(inp[0]), int(inp[1])):
    if esPrimo(i):
        print(i)
os.system(f"python menu.py")
raise SystemExit(0)
