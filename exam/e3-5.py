def gcd(x, y):
  return x if y == 0 else gcd(y, x % y)


a, b = map(int, input("请输入两个整数").split())
print(gcd(a, b))
