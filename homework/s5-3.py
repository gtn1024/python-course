def Sum(*args):
  sum = 0
  for arg in args:
    sum += arg
  return sum


ns = map(int, input().split())
print(Sum(*ns))
