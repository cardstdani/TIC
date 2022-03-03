while True:
    i = input("Introduce un valor a convertir: \n")
    if i == "q134":
        break
    i = i.split()
    if i[1] == "p":
        print(f"{int(i[0])*2.54} cm")
    if i[1] == "m":
        print(f"{int(i[0])*1609.34} m")
    if i[1] == "f":
        print(f"{(int(i[0]) -32)*(5/9)} c")
    if i[1] == "g":
        print(f"{int(i[0])*3.785} l")
    if i[1] == "o":
        print(f"{int(i[0])*28.35} gr")
    if i[1] == "l":
        print(f"{int(i[0])/2.205} kg")
