'''
题目内容：
请编写Python程序完成以下要求：
提示用户从键盘上输入一个有效的年份，
在屏幕上打印这个年份是否为闰年，
要求使用条件运算符完成程序中的功能。
条件运算符的语法为：
表达式1 if 表达式2 else 表达式3，
其中若表达式2的值为True，则整个算式的值为表达式1的值，
否则，整个算式的值为表达式3的值。

输入格式：
直接输入一个表示年份的整数，不需要给出提示性输出，即input()函数不要有任何参数

输出格式：
输出对上述年份的判断结果，具体格式请参考下方的输入样例1和输入样例2

输入样例1：
2000
输出样例1：
2000 is leap year.

输入样例2：
2100
输出样例2：
2100 is not leap year.
'''


def ck(y):
  return True if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 else False


y = int(input())
if ck(y):
  print("%d is leap year." % y)
else:
  print("%d is not leap year." % y)
