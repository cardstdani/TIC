while True:
    i = input("Introduce un número: \n")
    if i.isnumeric():
        i = int(i)
        if i == 0:
            break
        elif i > 0:
            print("par\n" if i%2 == 0 else "impar\n")
    else:
        print("Error;\n")
