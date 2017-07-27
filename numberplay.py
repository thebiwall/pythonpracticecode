#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

from string import c

def num_play(x,y):
    a = []
    for i in range(x,y):
        if (i%7 == 0) and (i%5 != 0):
            a.append(i)
    i = i + 1
    return a

num_play(2000, 3201)