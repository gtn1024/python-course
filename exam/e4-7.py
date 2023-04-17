a = [1, 4, 2, 4, 6, 7, 5, 4, 3, 2, 55, 7, 3, 2]
a.sort()
print(a)
while True:
  idx = int(input('请输入需要弹出的元素下标：'))
  try:
    a.pop(idx)
  except IndexError:
    print('超出索引')
    break
  print(a)
