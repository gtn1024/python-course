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


if __name__ == '__main__':
    zm = Student('zhangming', 20, 69, 88, 100)
    print(str(zm))

    yl = Student('杨雷', 21, 128, 128, 128)
    print(str(yl))
