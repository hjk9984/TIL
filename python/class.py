import sys

class Car:
    def __init__(self, color = None, speed = None) -> None:
        print('constructor')

    def __del__(self):
        print('destructor')     # 소멸자

    def Go():           # class method
        print('Car go')

    def Stop(self):     
        print('Car Stop')

    @staticmethod
    def static_test():
        print('static')

    @classmethod
    def class_test(cls):
        print(cls.__class__)


c = Car()

Car.Go()    # 클래스에서 호출할 때는 그냥 호출
#c.Go()     # 인스턴스가 부를 때는 Go(c), 인터프리터가 이렇게 만듬

c.Stop()    # Stop(c)
Car.Stop(c) # self가 있으면 클래스에서 부를 때 객체를 넣어줘야 함
#Car.Stop()

#----------------------
# instance method   : 객체가 있어야만 호출 가능
# static method     : 객체가 없어도 호출 가능(클래스에서 정의된 필드 사용 못함)
# Car.Stop() cpp와는 다르게 인스턴스에서 정적 메소드를 부를 수 없다,
# 클래스와 인스턴스에서 둘다 호출하기 위해서 데코레이터를 통해 만듬
Car.static_test()
c.static_test()

Car.class_test()    # Car.class_test(Car)
c.class_test()      # Car.class_test(c.__class__)

# 결국 정적 메소드를 만들떄 
# 클래스 정보가 필요하다 >> 클래스메소드 데코
# 필요 없다 >> 스테틱 메소드 데코


print('-' * 20)
#----------------------------------
class Point:
    def __init__(self) -> None:
        print('Point ctor')
        self.x = 0
        self.y = 0
        # 이렇게 하면서 __dict__에서 만듬

        self._a = 1
        self.__b = "private var"    # 인스턴스에서 사용할 수 있지만 네임 맹글링이 바뀜

    def __goo(self):
        print("__goo")


p1 = Point()
p2 = Point()

# 멤버 데이터 의도적으로 밖에서 만들기
p1.__dict__['x'] = 0
p1.z = 0

print(p1.__dict__)
print(p2.__dict__)

print(p1._a)
#print(p1.__b)
print(p1._Point__b) # not perfect private
p1._Point__goo()

print(sys.getsizeof(Point))
print(sys.getsizeof(p1))
print(sys.getsizeof(p2))

ct  = p1.__class__  # == cls type
p3 = ct()           # p3 = Point()


print('-' * 20)
#----------------------------------
# instance field:   객체별로 따로 보관되는 데이터
# static field:     모든 객체가 공유하는 데이터
class Reck:
    cnt = 0         # Reck.cnt = 0  >> Reck.__dict__에 저장
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y


r1 = Reck(1, 2)
r2 = Reck(3, 4)

print(Reck.__dict__)
Reck.test = 10      #Reck.__dict__['test'] = 10
print(Reck.__dict__)

# access static field
Reck.cnt = 10
print(r1.cnt)   # 읽기는 r1.__dict__으로 먼저 검색하고 없으면 Reckt.__dict__에서 검색 
# 위는 아무 이상이 없음

r2.cnt = 100    # 쓰기는 r2.__dict__에 저장
print(r1.__dict__)
print(r2.__dict__)
