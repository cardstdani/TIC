l = []
i = 0
while i < 3:
    inp = input("Introduce un número:\n")
    if inp.isnumeric():
        l.append(int(inp))
        i += 1
    else:
        print("Error;\n")

def merge(l1, l2):
    rl = []
    
    while l1 != [] or l2 != []:
        try:
            if l1[0] <= l2[0]:
                rl.append(l1[0])
                l1.pop(0)
            else:
                rl.append(l2[0])
                l2.pop(0)
        except:
            if l1 == []:
                m = min(l2)
                rl.append(m)
                l2.pop(l2.index(m))
            else:
                m = min(l1)
                rl.append(m)
                l1.pop(l1.index(m))
    return rl
    
def mergeSort(li):
    if len(li) <= 1:
        return li
    mid = len(li)//2
    return merge(mergeSort(li[:mid]), mergeSort(li[mid:]))

print(",".join([str(i) for i in mergeSort(l)]))

#Solución simple
l = []
i = 0
while i < 3:
    inp = input("Introduce un número:\n")
    if inp.isnumeric():
        l.append(int(inp))
        i += 1
    else:
        print("Error;\n")

print(",".join([str(i) for i in sorted(l)]))
