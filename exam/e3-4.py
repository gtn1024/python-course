def isPalindrome(n):
  return str(n) == str(n)[::-1]


n = int(input())
print(f"{n}是回文数" if isPalindrome(n) else f"{n}不是回文数")
