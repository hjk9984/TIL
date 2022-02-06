# https://realpython.com/primer-on-python-decorators/

import functools
import time

# in python, functions are first-class objects.
# it means functions can be passed around and used as arguments
# just like any other objects

def say_hi(name):
    return f"hi {name}"

def say_whatsup(name):
    return f"What's up {name}"

def greet_bob(func):
    return func("bob")

# functions are names without parentheses
# this means that only a reference to the function is passed.
print(greet_bob(say_hi))
print(greet_bob(say_whatsup))


# Returning functions from functions
def parent(num):
    def first_child():
        return "hi I am emma"
    
    def second_child():
        return "Call me Liam"
    
    if num == 1:
        return first_child
    else:
        return second_child

first = parent(1)   #this means returning a reference to the function first_child
print(first)


print("\n")
print('-'*30)
# Simple Decorators
# decorators wrap a function, modifying its behavior
def dec(func):
    def wrapper():
        print(func.__name__)
        func()
    return wrapper

def foo():
    print("simple dec")

func1 = dec(foo)
func1()


# @(pie) symbol
# if dec function is in another module,
# you can use @dec by from ~ import dec
@dec
def hoo():
    print("@ deco")

hoo()


print('-'*30)
# Decorating functions with arguments
def do_twice(func):
    def wrapeer(*args, **kargs):
        func(*args, **kargs)
        func(*args, **kargs)
    return wrapeer

# hoo is already wrapped by dec deco
# so do_trice call dec too.
hoo2 = do_twice(hoo)
hoo2()

@do_twice
def koo(name):
    print(f"hi {name}")
koo("bob")


# Returning values from decorated functions
def do_twice2(func):
    def wrapeer(*args, **kargs):
        func(*args, **kargs)
        # make sure the wrapper function returns the return value of the deco func
        return func(*args, **kargs)
    return wrapeer

@do_twice2
def joo(name):
    print(f"creating {name}")
    return "joo object"

print(joo("joo"))


print('-'*30)
# who are you really
# the function joo is inner function of do_twice2
# joo has gooten confused about its identity
# to fix this, decorators should use the @functools.wraps

def do_twice3(func):
    @functools.wraps(func)
    def wrapeer(*args, **kargs):
        func(*args, **kargs)
        return func(*args, **kargs)
    return wrapeer

def loo(name):
    print(f"hi {name}")
    return name

loo1 = do_twice2(loo)
loo1("kim")
print(loo1.__name__)
loo2 = do_twice3(loo)
loo2("kim")
print(loo.__name__)


print('-'*30)
# few real examples
# timer
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kargs):
        start = time.perf_counter()
        value = func(*args, **kargs)
        end = time.perf_counter()
        print(f"{func.__name__} run time : {end - start}")
        return value
    return wrapper

@timer
def timer_test(num):
    sum = 0
    for i in range(num):
        sum += i

timer_test(500000)

# debugging
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f" calling {func.__name__}, ({signature})")
        value = func(*args, **kwargs)
        print(f"func returns {value}")
        return value
    return wrapper

loo3 = debug(loo)
loo3("kim")


# Registering Plugins
# decoratoers don't have to wrap the cuntion they're decorating
# register decorator stores a reference to the decorated function
# you do not have to write an inner function or use @functools.wraps in this example 
# because you are returning the original function unmodified.
PLUGINS = dict()

def register(func):
    PLUGINS[func.__name__] = func
    return func

@register
def tmp1(name):
    return f"tmp1 {name}"

@register
def tmp2(name):
    return f"tmp2 {name}"

print(PLUGINS)
print(PLUGINS["tmp1"]("kim"))

# register is similar to globals()
#print(globals())

print("="*30)
print()