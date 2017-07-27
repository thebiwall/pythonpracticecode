# Write a function that returns the elements on odd positions (0 based) in a list

def odd_disp(x):
    output = []
    i = 0
    for i in x:
        if (i%2) > 0:
            output.append(x[i])
    i = i + 1
    return output
#assert solution([0,1,2,3,4,5]) == [1,3,5]
#assert solution([1,-1,2,-2]) == [-1,-2]