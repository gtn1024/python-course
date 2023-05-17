import math

class Student:
    def __init__(self, name: str, age: int, chinese: int, math: int, english: int):
        self.name = name
        self.age = age
        self.chinese = chinese
        self.math = math
        self.english = english
    
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    
    def get_course(self):
        return max(self.chinese, self.math, self.english)
    
    def __str__(self) -> str:
        return f'{self.name} {self.age} {self.get_course()}'

class HighSchoolStudent(Student):
    def __init__(self, name: str, age: int, chinese: int, math: int, english: int, physics: int, chemistry: int, biology: int, history: int, politics: int):
        super(HighSchoolStudent, self).__init__(name, age, chinese, math, english)
        self.physics = physics
        self.chemistry = chemistry
        self.biology = biology
        self.history = history
        self.politics = politics
    
    def get_average(self) -> int:
        return math.floor((self.chinese+self.math+self.english+self.physics+self.chemistry+self.biology+self.history+self.politics) / 8)
    
    def get_course(self):
        return max(self.chinese,self.math,self.english,self.physics,self.chemistry,self.biology,self.history,self.politics)

if __name__ == '__main__':
    zm = HighSchoolStudent('zhangming', 20, 69, 88, 100, 99, 99, 99, 99, 99)
    print(str(zm))
    print(zm.get_average())
    print(zm.get_course())

    yl = HighSchoolStudent('杨雷', 21, 128, 128, 128, 128, 128, 128, 128, 129)
    print(str(yl))
    print(yl.get_average())
    print(yl.get_course())
