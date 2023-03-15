Sn = 0
Hn = 100


def cal(n):
  global Sn, Hn
  if Hn == 100:
    Sn += Hn
  if n == 0:
    return
  Sn += Hn
  Hn /= 2
  cal(n - 1)


n = int(input())
cal(n)
print(f"Total of road is {Sn} meter")
print(f"The height is {Hn} meter")
