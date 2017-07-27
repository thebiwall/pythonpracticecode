def removeKFromList(l, k):
    i = 0
    j = 0
    b = []
    print(l)
    while i < len(l):
        if l[i] == k:
            b.append(i)
        i = i + 1
        while j < len(b):
            del l[b[j]]
            j = j + 1
    return l


l = [3, 1, 2, 3, 4, 5]
k = 3
removeKFromList(l, k)