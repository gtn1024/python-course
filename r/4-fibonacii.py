def fibonacii(x: int):
  if x == 0:
    return 0
  if x <= 2:
    return 1
  return fibonacii(x-1)+fibonacii(x-2)

if __name__ == '__main__':
  print(fibonacii(10))
