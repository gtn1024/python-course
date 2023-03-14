from math import sqrt

a, b, c = map(float, input("请输入三角形的三条边，以空格分隔：").split())
if a + b > c and a + c > b and b + c > a:
  p = (a + b + c) / 2
  s = sqrt(p * (p - a) * (p - b) * (p - c))
  print(f"三角形的面积为{s}")
else:
  print("不能构成三角形")
