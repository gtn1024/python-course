"""
题目内容：
编写程序完成以下要求：定义一个Student类，包含以下私有属性： 姓名、年龄、语文成绩、数学成绩、英语成绩（其中，每个科目的成绩类型为整数），且包含以下方法的定义：
（1）获取学生的姓名：get_name() 
（2）获取学生的年龄：get_age() 
（3）返回3门科目中最高的分数：get_maxScore() 
（4）返回3门科目的总成绩：get_totalScore()
完成类的定义以后，在主程序中接收键盘输入的学生信息，并使用该信息创建1个学生对象，计算输出该同学各科目成绩的最高分和总成绩。 

输入格式：
在一行内输入学生的姓名、年龄、语文成绩、数学成绩、英语成绩，用英文逗号分隔

输出格式：
参考输出样例输出该同学的各科成绩的最高分和总成绩

输入样例：
Tom,20,78,80,82

输出样例：
Tom's highest score in all subjects is 81, and his total score is 240.
"""
import math

class Student:
    def __init__(self, name, age, chinese, math, english):
        self.name = name
        self.age = age
        self.chinese = chinese
        self.math = math
        self.english = english
    
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    
    def get_maxScore(self):
        return max(self.chinese, self.math, self.english)
    
    def get_totalScore(self):
        return self.chinese+self.math+self.english
    
    def __str__(self):
        return "%s's highest score in all subjects is %d, and his total score is %d." % (self.name, self.get_maxScore(), self.get_totalScore())
    
if __name__ == '__main__':
    name, age, chinese, math, english = input().split(',')
    zm = Student(name, int(age), int(chinese), int(math), int(english))
    print(str(zm))
