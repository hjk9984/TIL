def add_emotion(func):
                        # 이 부분은 최초에 한번만 실행
    def inner():
        print(':D', end=' ')
        func()

    return inner

def say_hi():
    print("hi")

@add_emotion        #say_hello = add_emotion(say_hello)
def say_hello():
    print('hello')


say_hi = add_emotion(say_hi)
say_hi()

say_hello()

# The core feature of inner functions is their ability to access variables 
# and objects from their enclosing function even after this function has returned. 
# The enclosing function provides a namespace that is accessible to the inner function


def deco1(func):
    def inner():
        x = 3
        func()
    return inner

tmp1 = deco1(say_hello)
print(tmp1.__closure__)
print(tmp1.__dict__)


#https://stackoverflow.com/questions/14413946/what-exactly-is-contained-within-a-obj-closure
def foo():
    def bar():
        print(spam)

    spam = 'ham'
    bar()
    spam = 'eggs'
    bar()
    return bar

b = foo()
b()


# deco2
print('-'*30)

from functools import wraps

def add_emotion2(func):

    def inner(*args, **kwargs):
        print(':D', end=' ')
        result = func(*args, **kwargs)
        return result

    return inner

@add_emotion2
def say_hi2(name):
    print(f'hello {name}')

say_hi2('kim')
# this skill is called by perfect forwarding in cpp


def add_emotion3(func):

    @wraps(func)
    def inner(*args, **kwargs):
        print(':D', end=' ')
        result = func(*args, **kwargs)
        return result

    return inner

@add_emotion3
def say_hi3(name):
    '''say hello func'''
    print(f'hello {name}')

# by using wraps, retain the metadata of function
print(say_hi3.__name__)
print(say_hi3.__doc__)


#deco ex 1
import time

def chronometry(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"elapse time : {end - start}")
        return result
    return inner

@chronometry
def f1():
    s = 0
    for n in range(10000000):
        s = s+ n
    return s

@chronometry
def f2():
    s = sum(range(10000000))
    return s

print(f1())
print(f2())


# deco 2
def trace(func):
    num = 0
    def inner(*args, **kwargs):
        nonlocal num            # 중요
        num = num + 1
        print(f'called {func.__name__}, {num} times')
        return func(*args, **kwargs)
    return inner

@trace
def foo(a, b): pass

@trace
def goo(a):pass

foo(1, 2)
goo(1)
goo(2)
foo(3, 4)
print(foo.__closure__)
print(goo.__closure__)


# deco4
# 인자가 있는 데코
print('-'*30)
def add_emotion4(emotion = ':D'):

    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            print(emotion, end=' ')
            result = func(*args, **kwargs)
            return result

        return inner
    
    return decorator

# say_hi4 = add_emotion('^-^')(say_hi4)
@add_emotion4('^-^')
def say_hi4(name):
    print(f"hi {name}")

say_hi4('lee')
print(say_hi4.__closure__)


def add_emotion5(emotion = ':D'):

    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            print(emotion, end=' ')
            result = func(*args, **kwargs)
            return result
        

        # 중간에 이모티콘 바꾸게끔 하는 법
        def set_emotion(emo):
            nonlocal emotion
            emotion = emo
        inner.set_emotion = set_emotion

        return inner
    
    return decorator

# say_hi4 = add_emotion('^-^')(say_hi4)
@add_emotion5('^-^')
def say_hi5(name):
    print(f"hi {name}")

say_hi5.set_emotion("><")
say_hi5("hi5")


# deco 4
# 커링: 인자가 2개인 함수를 인자가 한개인 함수의 연속적인 호출로 사용
#      인자가 5개인 함수를 3개 2개의 인자로 나누어 호출
from functools import partial
def register(obj, func = None):
    if func is None:
        return partial(register, obj)   # >> 커링
    
    setattr(obj, func.__name__, func)
    return func

def inner():
    pass

@register(inner)
def set_emotion():
    print('set_emotion')

inner.set_emotion()
set_emotion()


def add_emotion6(emotion = ':D'):

    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            print(emotion, end=' ')
            result = func(*args, **kwargs)
            return result
        

        # 중간에 이모티콘 바꾸게끔 하는 법
        @register(inner)
        def set_emotion(emo):
            nonlocal emotion
            emotion = emo
        #inner.set_emotion = set_emotion

        return inner
    
    return decorator


@add_emotion6('-_-')
def say_hi6(name):
    print(f"hi {name}")

say_hi6("6kkim6")
say_hi6.set_emotion("XD")
say_hi6("6kim6")
