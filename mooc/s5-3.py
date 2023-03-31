"""
题目内容：
请编写Python程序完成以下要求：
提示用户从键盘上输入一个数num，
判断该数num是否为回文数。
（所谓回文数就是一个正数顺过来和反过来都是一样的，比如123321、15851等等，就是回文数）

输入格式：
输入一个正整数，不需要给出提示性输出，即input()函数不要有任何参数

输出格式：
参考下方输出样例，输入判定结果

输入样例1：
123321

输出样例1：
12321 is palindrome number.

输入样例2：
123456

输出样例2：
123456 is not palindrome number.
"""


def check(x):
  return x == str(x)[::-1]


if __name__ == '__main__':
  x = input()
  if check(x):
    print("%s is palindrome number." % x)
  else:
    print("%s is not palindrome number." % x)
