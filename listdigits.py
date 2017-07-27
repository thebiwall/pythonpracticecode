# Write a function that takes a number and returns a list of its digits

def list_dig(x):
    x = str(x)
    output = list(x)
    a = len(output)
    final = []
    for i in range(a):
        final.append(int(output[i]))
    i = i + 1
    return final


assert list_dig(123) == [1,2,3]
assert list_dig(400) == [4,0,0]