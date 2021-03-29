# super(): 자식클래스에서 부모클래스의 내용을 사용하고 싶은 경우
# super().부모클래스내용

class Animal():
    def __init__(self, name):
        self.name = name

    def walk(self):
        print('걷는다.')

    def eat(self):
        print('먹는다.')

    def greet(self):
        print('{}가 인사한다.'.format(self.name))


class Human(Animal):
    def __init__(self, name, hand):
        super().__init__(name)
        self.hand = hand

    def wave(self):
        print('{}을 흔들면서'.format(self.hand))

    def greet(self):
        self.wave()
        super().greet()


person = Human('흥민이', '오른손')
person.greet()
