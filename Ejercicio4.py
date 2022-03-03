while True:
    i = input("Introduce un número: \n")
    if i.isnumeric():
        i = int(i)
        if i >= 1 and i <= 100:
            s = ""
            for a in range(1, 11):
                s += f"{a} x {i} = {a*i}\n"
            print(s)
            break
        else:
            continue
    else:
        print("Error;\n")
