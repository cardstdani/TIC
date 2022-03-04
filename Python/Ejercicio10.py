while True:
    inp = input("Introduce una secuencia de números enteros separados por un espacio y que acabe en 0:\n")
    if inp[-1] != "0":
        print("La secuencia debe acabar en 0\n")
    else:
        inp = [int(i) for i in inp[:-1].split()]
        current = inp[0]
        creciente = True
        for i in inp:
            if i >= current:
                current = i
            else:
                creciente = False
                break
        print("\nCreciente" if creciente else "\nNo creciente")
