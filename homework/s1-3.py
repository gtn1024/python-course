"""
输入三角形的三条边a, b, c，计算三角形的面积。
"""

import math

a, b, c = map(float, input().split())
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(s)
