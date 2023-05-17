class Dog:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def wangwang(self):
        print('wang! wang!')

if __name__ == '__main__':
    dog = Dog('旺财', '黄色', 10)
    dog.wangwang()
