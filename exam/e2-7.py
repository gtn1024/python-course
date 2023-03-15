import math

n = int(input("请输入一个整数："))
if n <= 1:
  print(f"{n}不是素数")
elif n == 2:
  print(f"{n}是素数")
else:
  ed = math.sqrt(n)
  flg = False
  for i in range(2, math.ceil(ed) + 1):
    if n % i == 0:
      print(f"{n}不是素数")
      flg = True
      break
  if not flg:
    print(f"{n}是素数")
