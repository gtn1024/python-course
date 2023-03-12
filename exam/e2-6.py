def check(x):
  n = x
  a = n // 100
  n %= 100
  b = n // 10
  n %= 10
  c = n
  return a * a * a + b * b * b + c * c * c == x


for i in range(100, 1000):
  if check(i):
    print(i)
