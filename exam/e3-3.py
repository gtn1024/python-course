l = [0] * 50


def f(n):
  if l[n] != 0:
    return l[n]
  if n == 1 or n == 2:
    l[n] = 1
  else:
    l[n] = f(n - 1) + f(n - 2)
  print(l[n], end=' \n'[n == 20])
  return l[n]


f(20)
