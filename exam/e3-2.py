import random
import math


def gym(m, n):
  return m if n == 0 else gym(n, m % n)


a = math.ceil(random.random() * 100)
b = math.ceil(random.random() * 100)
print(f"{a}和{b}互质" if gym(a, b) == 1 else f"{a}和{b}不互质")
