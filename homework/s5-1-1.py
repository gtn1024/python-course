def f(n):
  res = 0
  for i in range(1, n + 1):
    res += 1 / i
  return res


n = int(input())
print(f(n))
