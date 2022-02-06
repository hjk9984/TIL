from dataclasses import dataclass
from decorator import debug, timer, do_twice

import functools
import time

# some commonly used decorators thaat are even built-ins in python
# are @clasmethod, @staticmethod, @property.
# The @classmethod and @staticmethod decorators are used to define methods inside a class namespace that are not connected
# to a particular instance of that class.
# The @property decorator is used to customize getters and setters for class attributes.


class TimeWaster:
    @debug
    def __init__(self, max_num):
        self .max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])


tw = TimeWaster(100)
# tw.waste_time(999)


# the way to use decorators on classes is to decorate the whole class


@dataclass
class PlayingCard:
    rank: str
    suit: str

# A common use of class decorators is to be a simpler alternative to some use-cases of metaclasses.
# In both cases, you are changing the definition of a class dynamically.


@timer
class TimeWaster:
    def __init__(self, max_num):
        self .max_num = max_num

    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])


# above class is equal to TimeWaster = timer(TimerWaster)
# timer only measures the time it takes to instantiate the class
tw = TimeWaster(1000)
# tw.waste_time(999)      # >> None


print('-'*30)
# Nesting Decorators


@debug
@do_twice
def greet(name):
    print(f"greet nest {name}")


greet("kim")
print()


@do_twice
@debug
def greet2(name):
    print(f"greet2 nest {name}")


greet2("kim")


print('-'*50)
# Decorators with arguments


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat

# it looks little messy, but we have only put
# the same decorator pattern you have seen
# @repeat(num_times) == @decortator_repeat


@repeat(num_times=3)
def greet3(name):
    print(f"greet3 {name}")


greet3("kim")


print('-'*30)
# Stateful Decorators


def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0   # >> function attributes
    return wrapper_count_calls


@count_calls
def say_whee():
    print("Whee!")


say_whee()
say_whee()

print('-'*30)
# appendix: function attributes
# functions are objects, so they have attributes like other objects


def ioo():
    pass


setattr(ioo, 'a', 23)
ioo.k = 32
print(ioo.a)
print(ioo.k)


# Classes as Decorators
# the typical way to maintain state is by using classes
# if decorator is a class, it needs to take func as an argument in its .__init__()

# The .__init__() method must store a reference to the function and can do any other necessary initialization.
# The .__call__() method will be called instead of the decorated function.
# you need to use the functools.update_wrapper() function instead of @functools.wraps

# @func1
# def func2        ==      func2 = func1(func2)

class CountCalls:
    def __init__(self, func) -> None:
        functools.update_wrapper(self, func)    # it plays like wraps(func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of ({self.func.__name__!r})")
        return self.func(*args, **kwargs)


@CountCalls
def say_whee1():
    print("class whee!")


say_whee1()
say_whee1()


# practice

def arg_deco(num_limits=2):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if(func.cnt >= num_limits):
                print("the number of function calling is limited")
                return
            func.cnt += 1
            print(f"{func.__name__} is calling ...")
            return func(*args, **kwargs)
        func.cnt = 0
        return wrapper
    return deco


@arg_deco(2)
def test_cnt():
    print("test_cnt")


test_cnt()
test_cnt()
test_cnt()
test_cnt()
