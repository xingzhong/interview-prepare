def permute(x):
  if len(x) == 1:
    yield x
  else:
    for perm in permute(x[1:]):
      for i in range(len(x)):
        yield perm[:i] + x[0:1] + perm[i:]


for p in permute('abcd'):
  print p
