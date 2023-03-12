def gcd(x, y):
  return x if y == 0 else gcd(y, x % y)


def lcm(x, y):
  return x * y // gcd(x, y)


a, b = map(int, input("请输入两个数：").split())
aa = gcd(a, b)
bb = lcm(a, b)
print(f"最大公约数为{aa}，最小公倍数为{bb}")
