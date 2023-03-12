import math


def prime(x):
  if x <= 1:
    return False
  ed = math.sqrt(x)
  for i in range(2, math.ceil(ed)):
    if x % i == 0:
      return False
  return True


n = int(input("请输入一个整数："))
if prime(n):
  print(f"{n}是素数")
else:
  print(f"{n}不是素数")
