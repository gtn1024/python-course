"""
题目内容：
请编写Python程序完成以下要求：
编写函数，输出Fibonacci数列的前10项，
其中Fibonacci数列满足以下要求：F0=1，F1=1，……，Fn=Fn-1+Fn-2。

输入格式：
没有输入

输出格式：
数列元素之间用英文逗号分隔

输入样例：
无

输出样例：
1,1,2,……
"""

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
for i in range(10):
    print(fib(i),end=',\n'[i==9])
