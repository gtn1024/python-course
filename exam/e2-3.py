a, b = map(int, input("请输入两个数：").split())
aa = 0
x = a
y = b
while y != 0:
  temp = x % y
  x = y
  y = temp
  aa = x

x = a
y = b
re = 0
c = x if x > y else y
while c <= a * b:
  if c % a == 0 and c % b == 0:
    re = c
    break
  c += 1
bb = re

print(f"最大公约数为{aa}，最小公倍数为{bb}")
