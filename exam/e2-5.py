def check(s):
  x = 0
  y = len(s) - 1
  while x <= y:
    if s[x] != s[y]:
      return False
    x += 1
    y -= 1
  return True


s = input("请输入一个正整数：")
print("是回文数" if check(s) else "不是回文数")
