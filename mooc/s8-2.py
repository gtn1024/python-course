"""
题目内容：
编写程序完成以下要求：定义HighSchoolStudent（高中生）类，继承上题中的Student类，增加化学成绩、物理成绩、生物成绩、历史成绩、政治成绩5个私有属性，以及以下两个方法：
（1）返回8门课程平均分的方法：get_average()
（2）返回8门课程中最高分的方法：get_ maxScore ()
完成类的定义以后，在主程序中接收键盘输入的学生信息，并使用该信息创建1个学生对象，并计算输出该同学各科目成绩的平均分（保留2位小数）和最高分。

输入格式：
在一行内输入学生的姓名、年龄、语文成绩、数学成绩、英语成绩、化学成绩、物理成绩、生物成绩、历史成绩、政治成绩，用英文逗号分隔

输出格式：
参考输出样例输出该同学的各科成绩的平均分和最高分

输入样例：
Rose,20,60,70,80,90,100,90,80,70

输出样例：
Rose's average score in all subjects is 80.00, and the highest score is 100.
"""

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
    
class HighSchoolStudent(Student):
    def __init__(self, name, age, chinese, math, english, chemistry, physics, biology, history, politics):
        super().__init__(name, age, chinese, math, english)
        self.chemistry = chemistry
        self.physics = physics
        self.biology = biology
        self.history = history
        self.politics = politics
    
    def get_average(self):
        return (self.chinese+self.math+self.english+self.chemistry+self.physics+self.biology+self.history+self.politics)/8
    
    def get_maxScore(self):
        return max(self.chinese, self.math, self.english, self.chemistry, self.physics, self.biology, self.history, self.politics)
    
    def __str__(self):
        return "%s's average score in all subjects is %.2f, and the highest score is %d." % (self.name, self.get_average(), self.get_maxScore())
    
if __name__ == '__main__':
    name, age, chinese, math, english, chemistry, physics, biology, history, politics = input().split(',')
    zm = HighSchoolStudent(name, int(age), int(chinese), int(math), int(english), int(chemistry), int(physics), int(biology), int(history), int(politics))
    print(str(zm))
    