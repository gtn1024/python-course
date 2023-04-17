"""
编写程序，
用户输入一段英文，
然后输出这段英文中所有长度为3个字母的单词。
(假设单词间只用空格分隔)
"""
if __name__ == '__main__':
  words = input('请输入英文单词，用空格分隔：').split()
  for i in range(len(words)):
    if len(words[i]) == 3:
      print(words[i])

# The left-hand side vertices represent tweets the right-hand side vertices represent hashtags and the edges represent content association
