def quickSort(x):
  if len(x) < 1:
    return []
  pivot = x[0]
  less = filter(lambda x: x<=pivot, x[1:])
  greater = filter(lambda x: x>pivot, x[1:])
  return quickSort(less)+[pivot]+quickSort(greater)


from random import randint
test = map(lambda x : randint(1,100), range(30))
print test
print quickSort(test)
