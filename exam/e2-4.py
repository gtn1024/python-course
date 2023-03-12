n = int(input("请输入三角形的行数："))
for i in range(1, n + 1):
  for j in range(i - 1):
    print(" ", end="")
  for j in range(2 * (n - i + 1) - 1):
    print("*", end="")
  print()
