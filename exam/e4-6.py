import os

mp = dict()
f = open(f'{os.path.dirname(__file__)}/e4-6.txt', 'r', encoding='utf-8')
f.seek(0)
lines = f.read().splitlines()
for line in lines:
  person = line.split('，')
  name = person[0]
  phone = person[1]
  mp[name] = phone


def query():
  name = input("请输入需要查询的姓名：")
  print(mp[name] if mp.get(name, -1) != -1 else 'Not found')


if __name__ == '__main__':
  while True:
    query()
