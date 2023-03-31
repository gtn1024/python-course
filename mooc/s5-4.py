"""
题目内容：
请编写Python程序完成以下要求：
定义函数用于求两个整数的最大公约数和最小公倍数，
并编写主程序，
提示用户从键盘上输入两个正整数，
通过调用你定义的函数完成计算，
并返回结果。

输入格式：
输入两个正整数，用英文逗号隔开，不需要给出提示性输出，即input()函数不要有任何参数

输出格式：
输出最大公倍数和最下公约数，用英文逗号分隔

输入样例：
15,20

输出样例：
5,60
"""


def gcd(a, b):
  return a if b == 0 else gcd(b, a % b)


def lcm(a, b):
  return a * b / gcd(a, b)


if __name__ == '__main__':
  a, b = map(int, input().split(','))
  print("%d,%d" % (gcd(a, b), lcm(a, b)))
