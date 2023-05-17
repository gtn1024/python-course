"""
题目内容：
请编写Python程序完成以下要求：从键盘上输入一句英文句子，统计其中出现次数最多的字母。

输入格式：
一条英文句子，其中可以包括标点符号和英文大小写，不需要给出提示性输出，即input()函数不要有任何参数

输出格式：
输出出现次数最多的字母对应的小写字母形式

输入样例：
This is a banana.

输出样例：
a
"""

d = dict()
mx = 0
ans = ''
for i in input():
  if i.isalpha():
    d[i.lower()] = d.get(i.lower(),0)+1

for i in d:
  if d[i]>mx:
    mx=d[i]
    ans=i

print(ans)
