"""
题目内容：
请编写Python程序完成以下要求：
以每行5个的形式输出100以内的所有素数。

输入格式：
没有输入

输出格式：
在循环结构中，使用语句print("{:2}".format(num),end="")输出每一个素数，每输出5个素数后输出一个换行

输入样例：
无

输出样例：
  2  3  5  7 11
 13 17 19 23 29
…
"""
from math import sqrt, ceil


def check(x):
  if x == 2:
    return True
  xx = ceil(sqrt(x))
  for i in range(2, xx + 1):
    if x % i == 0:
      return False
  return True


if __name__ == '__main__':
  cnt = 0
  for i in range(2, 101):
    if check(i):
      cnt += 1
      print("{:3}".format(i), end="")
      if (cnt % 5 == 0):
        print()
