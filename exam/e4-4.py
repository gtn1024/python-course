"""
数字重复统计: 
1). 随机生成1000个整数;
2). 数字的范围[20, 100]
3). 升序输出所有不同的数字及其每个数字重复的次数。
（要求1000个整数存放在列表中，统计的结果存放在字典）
"""
import random
import math

st = set()
mp = dict()
for i in range(1000):
  t = 20 + math.floor(random.random() * 80)
  st.add(t)
  mp[t] = mp.get(t, 0) + 1
for i in st:
  print(f"{i} - {mp[i]}个", end='\t')
  if (i + 1) % 5 == 0:
    print()
