def inverso(n):
    return int(str(n)[::-1])

def capicua(n):
    return n == inverso(n)

while True:
    inp = int(input("Introduce un número:\n"))
    
    if inp < 0:
        break
    print(f"El número {inp} es capicua" if capicua(inp) else f"El número {inp} es capicua")
