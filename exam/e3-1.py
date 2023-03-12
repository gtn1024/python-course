import math


def judgePrime(n):
  if n <= 1:
    return False
  ed = math.sqrt(n)
  for i in range(2, math.ceil(ed)):
    if n % i == 0:
      return False
  return True


for i in range(4, 2000, 2):
  for j in range(2, i):
    a = j
    b = i - j
    if (judgePrime(a) and judgePrime(b)):
      print(f"{i} = {a} + {b}")
      break
