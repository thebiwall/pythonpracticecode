# Write a function that returns the cumulative sum of elements in a list

def list_cumm(x):
    output = []
    i = 0
    j = 0
    a = len(x)
    print(a)
    for i in range(a):
        j = j + x[i]
        output.append(j)
        print(output)
    i = i + 1
    return output


#assert list_cumm([1,1,1]) == [1,2,3]
#assert list_cumm([1,-1,3]) == [1,0,3]