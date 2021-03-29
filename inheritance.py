# 상속(inheritance)
# 상속하는 클래스를 부모 클래스
# 상속받는 클래스를 자식 클래스
# 자식 클래스가 부모 클래스의 내용을 가져다 쓸 수 있는 것

# 부모 클래스
class Animal():
    def walk(self):
        print('걷는다.')

    def eat(self):
        print('먹는다.')

# 자식 클래스


class Human(Animal):
    def wave(self):
        print('손을 흔든다.')

# 자식 클래스


class Dog(Animal):
    def wag(self):
        print('꼬리를 흔든다.')


person = Human()
person.eat()
person.walk()
person.wave()

dog = Dog()
dog.eat()
dog.walk()
dog.wag()
