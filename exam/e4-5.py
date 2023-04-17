"""
编写程序制作英文学习词典，
词典有3个基本功能：
添加、查询和退出。
程序读取源文件路径下的txt格式文件。
词典存储方式为“英文单词 中文释义”，
每行仅有一对中英释义。
程序会根据用户的选择进入相应的功能模块，
并显示相应的操作提示。
"""
import os

mp = dict()
f = open(f'{os.path.dirname(__file__)}/e4-5.txt', 'a+', encoding='utf-8')
f.seek(0)
lines = f.read().splitlines()
for line in lines:
  word = line.split(' ')
  eng = word[0]
  chi = word[1]
  mp[eng] = chi


def add():
  eng = input("请输入英文单词：")
  if mp.get(eng, -1) != -1:
    print("已存在！！！")
    return
  chi = input("请输入中文含义：")
  mp[eng] = chi
  f.write(f"{eng} {chi}\n")
  f.flush()


def query():
  word = input("请输入你要查询的单词：")
  print(mp[word] if mp.get(word, -1) != -1 else '没有这个单词')


def menu():
  print("1. 添加")
  print("2. 查询")
  print("3. 退出")
  o = int(input("请输入："))
  if o == 1:
    add()
  elif o == 2:
    query()
  else:
    f.close()
    exit(0)


if __name__ == '__main__':
  while True:
    menu()
