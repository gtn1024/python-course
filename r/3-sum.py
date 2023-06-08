def add(x: int):
  if x == 0:
    return 0
  return add(x-1) + x

if __name__ == '__main__':
  print(add(100))
