l = []
for i in range(3):
    inp = input("Introduce un número:\n")
    if inp.isnumeric():
        l.append(inp)
    else:
        print("Error;\n")

def merge(li1, li2):
    rl = []
    
    i, j = 0, 0
    while i < len(li1) and j < len(li2):
        if li1[i] <= li2[j]:
            rl.append(li1[i])
            i += 1
        else:
            rl.append(li2[j])
            j += 1
    return rl
            
    
def mergeSort(li):
    if len(li) <= 1:
        return li
    return merge(mergeSort(li[:len(li)//2]), mergeSort(li[len(li)//2:]))

print(",".join(mergeSort(l)))
