class Base :
    def __init__(self):
        self.x = 100
    
    def print(self):
        print(self.x)

    def foo(self):
        print('Base foo')

    def goo(self):
        print('Base goo')


class Derived(Base):
    # 파생클래스의 init 함수에서 기반 클래스의 init 함수를 명시적으로 호출해야한다.
    def __init__(self):
        super().__init__()


    def goo(self):
        print('Derived goo')

        # 기반 클래스 호출하는 법
        Base.goo(self)
        super().goo()   # method resoultion order의 순서에 따라 클래스 선택

d = Derived()
d.foo()
d.goo()


print('-'*30)
# 다중 산속
# super init default >> super(self.__class__, self)
class Base1:
    def __init__(self):
        print('Base1 __init__')


class A:
    def __init__(self):
        print('A __init__')
        Base1.__init__(self)

    def foo(self):
        print('A foo')


class B(Base1):
    def __init__(self):
        print('B __init__')
        Base1.__init__(self)

    def foo(self):
        print('B foo')

    # 상속 불가)
    def __hoo(self):
        pass;

class C(A, B):
    def __init__(self):
        print('C __init__')
        A.__init__(self)
        B.__init__(self)
        # super().__init__()으로 했으면 mro 때문에 A의 init을 호출

    def __hoo(self):
        pass


c = C()
c.foo()
print(C.mro())  #다중상속 시 메소드를 찾는 순서

# super(type, obj).func()
# c 객체에 대해ㅔ서 foo를 부를 건데 A의 부모에서 찾아라
super(A, c).foo()   # B.foo(c)
super(C, c).foo()   # A.foo(c)

b = B()
print(dir(c))
print(dir(b))



# http://www.srikanthtechnologies.com/blog/python/mro.aspx
# when in MRO we have a super class before subclass then it must be removed from that position in MRO.
