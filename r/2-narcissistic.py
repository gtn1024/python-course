def isNarcissistic(x: int):
  if x < 100 or x >= 1000:
    raise ValueError('Value should be [100, 1000)')
  a = x // 100
  b = x // 10 % 10
  c = x % 10
  return a **3 + b**3 + c**3 == x

if __name__ == '__main__':
  for i in range(100, 1000):
    if isNarcissistic(i):
      print(i)
