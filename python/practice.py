from functools import wraps
import sys

def unpacked_return():
    return 1,2,3,4

def none_return():
    pass

a, *b, c = unpacked_return()
print(a, b, c)
print(a, *b, c)

print(none_return())


def only_arg(a, /, b, *, c):
    print('only arg : ', a, b, c)

only_arg(1, 2, c=3)
only_arg(1, b=2, c=3)

tmp_dict = {'b': 2, 'c': 3}
only_arg(5, **tmp_dict)


def default_print(a, b, c):
    print(a, b, c)

tmp_dict['a'] = 10
default_print(**tmp_dict)
default_print(*tmp_dict)
default_print(*[1, 2, 3])

def add(x: int, y:int) -> int:
    return x + y

print(hex(id(add)))
print(sys.getsizeof(add))

# 함수 객체의 attributes
def foo(a= 10, b= 20, *, c=30, d=40):
    '''
        explaination of foo function
    '''
    y = 0
    def inner():
        nonlocal y
    return inner

print(foo.__doc__)
print(foo.__name__)
print(foo.__qualname__)
print(foo.__defaults__)
print(foo.__kwdefaults__)

f = foo()
print(f.__closure__)
print(foo.__closure__)

print(foo.__dict__)
foo.__dict__['x'] = 1000
foo.z = 900
print(foo.__dict__)
def goo():
    return 10

foo.goo = goo
print(foo.goo())
print(foo.goo == goo)


def add_sharp(s=[]):
    s.append('#')
    return s


s1 = [1, 2, 3]
print( add_sharp(s1) )

print(add_sharp.__defaults__)
print(add_sharp())

print(add_sharp.__defaults__)
print(add_sharp())

print(add_sharp.__defaults__)
print(add_sharp())

# 파이썬은 함수를 정의할 때 default parameter를 정의한다.
# 호출할 때마다 정의하는 것이 아니기 때문에 이 default parameter가 mutable하면
# 변화될 수 있다.




def add_emoticon(func):
    ''' emo emo'''
    y = 0
    print(id(y))
    @wraps(func)
    def inner(*args, **kwargs):
        x = 3
        print("XD ", end='')
        result = func(*args, **kwargs)
        return result   
    return inner

@add_emoticon
def say_hi(name):
    ''' hihi '''
    print(f"hihi {name}")

print(say_hi.__closure__)
print(say_hi.__dict__)
print(say_hi.__name__)
print(say_hi.__doc__)


def add_emoticon2(emoticon="XD "):
    def wrapper(func):
        print(hex(id(func)))
        print(f"decorate {func.__name__}")
        @wraps(func)
        def inner(*args, **kwargs):
            print(emoticon, " ", end='')
            result = func(*args, **kwargs)
            return result

        def set_emotion(emo):
            nonlocal emoticon
            emoticon = emo
        # function 객체에 추가
        inner.set_emotion = set_emotion
        
        return inner

    return wrapper

@add_emoticon2("T . T")
def say_hi2(name):
    print(f"hihi {name}")

say_hi2("lee")
print(say_hi2.__closure__)


from functools import partial
def register(obj, func = None):
    if func is None:
        return partial(register, obj)   
        # register(obj)(func) == register(obj, func)

    setattr(obj, func.__name__, func)
    return func

s1 = ['banana', 'kiwi', 'apple']
print(sorted(s1, key=lambda x: x[2]))

x = 10
f1 = lambda y : x+y
f2 = lambda y, x=x : x+y    # default arg is defined as the function is defined
x = 20
print(f1(10), f2(10))


class Car:
    def go():
        print('Car go')
    
    def stop(self):
        print('Car stop')

    @staticmethod
    def static_test():
        print('static')

    @classmethod
    def class_test(cls):
        print(cls.__class__)

c = Car()
Car.go()
c.stop()
Car.stop(c)

Car.static_test()
c.static_test()
Car.class_test()
c.class_test()

ct = c.__class__
c2 = ct()
c2.class_test()

class Reck:
    cnt = 0
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

r1 = Reck(1,2)
r2 = Reck(3,4)

print(Reck.__dict__)
Reck.test = 10
print(Reck.__dict__)
print(r1.cnt)

r2.cnt = 100
print(r1.__dict__)
print(r2.__dict__)
