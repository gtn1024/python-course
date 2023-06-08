import math

def isPrime(x: int):
  if x <2:
    return False
  if x == 2:
    return True
  for i in range(3, math.ceil(math.sqrt(x))+1):
    if x % i == 0:
      return False
  return True

if __name__ == '__main__':
  for i in range(100):
    print(f'{i} {isPrime(i)}')
