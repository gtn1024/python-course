"""
输入体重（单位kg）、身高，计算BMI。

体重指数（BMI）计算公式=体重（千克）/身高的平方（平方米）。
"""
w, h = map(float, input().split())
bmi = w / h / h
print(bmi)
