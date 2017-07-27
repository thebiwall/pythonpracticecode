def firstDuplicate(a):
  i=0
  j=0
  b=[]
  while i < len(a):
      if a.count(a[i]) > 1:
        j = i + 1
        while j < len(a):
          if a[j] == a[i]:
            b.append(j)
          j = j + 1
      i = i + 1
  if b == []:
    return -1
  else:
    print (b)
    return a[min(b)]


a = [2, 3, 3, 1, 5, 2]

firstDuplicate(a)