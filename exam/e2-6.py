for i in range(100, 1000):
  n = i
  a = n // 100
  n %= 100
  b = n // 10
  n %= 10
  c = n
  if a * a * a + b * b * b + c * c * c == i:
    print(i)
