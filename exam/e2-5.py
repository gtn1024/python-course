s = input("请输入一个正整数：")
flg = False
for i in s:
  if i not in "0123456789":
    print("输入错误")
    flg = True
    break

if not flg:
  if s == str(s)[::-1]:
    print("是回文数")
  else:
    print("不是回文数")
