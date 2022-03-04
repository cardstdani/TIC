for i in range(100, 1000):
    if i == (sum([int(a)**3 for a in str(i)])):
        print(i)
