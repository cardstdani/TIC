import os
def esPrimo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

inp = input("""
Menu, elige una de las 3 opciones:
1)Números primos entre 2 naturales
2)Primer número primo mayor que un natural dado
3)Cantidad de números primos menores que un natural dado
""")

os.system(f"python opcion{int(inp)}.py")
raise SystemExit(0)
