def foo():
    return [1, 2, 3, 4]

def foo1():
    return 1, 2, 3, 4   #(1,2,3,4)

def foo2():
    print('foo2')

a, *b, c = foo()
print(a, b, c)

res = foo1()
a, *b, c = foo1()
print(res)
print(a, b, c)

# if function doesn't return,
# return None
print(foo2())


def hoo(a, b, c):
    print(a, b, c)

# positional argument
hoo(1, 2, 3)

# keyword argument
hoo(1, b=2, c=3)

#hoo(1, b=2, 3)  >> error

# only pos arg before / (position only arg)
# only key arg after *  (keyword only arg)
def hoo2(a, /, b, *, c):
    print("hoo2", a, b, c)

#hoo2(1, 2, 3)      >>error
#hoo2(a=1, b=2, c=3)>>error
hoo2(1, 2, c=3)
hoo2(1, b=2, c=3)

# def f2(a, b=0, *, c):
# this doesnt raise error 


print("-"*30)
s = [1, 2, 3]
t = (1,2,3)
d = {'a':1, 'b':2, 'c':3}
# unpacking
# hoo(s)    >>error
hoo(*s)     # hoo(1, 2, 3)
hoo(*t)     # hoo(1, 2, 3)
hoo(*d)     # hoo('a', 'b', 'c')
hoo(**d)    # hoo(a=1, b=2, c=3)    keyword should be corresponded

def hoo3(a, *b):    #*b means get arg as tuple
    print(a, b)

hoo3(1, 2, 3)
hoo3(1, 2)
hoo3(1)


def hoo3(a, *b, c):    # c is keyword only arg
    print(a, b)
# hoo3(1,2,3,4) >> error
hoo3(1,2,3,c=4)

# parameter packing
# *args get only positional args
def hoo4(*args):
    print(args)
# hoo4(1,2,3, a=10) #>> error


def hoo5(**kwargs):
    print(kwargs)
# hoo5(1, a=10, b=20) #>> error


import time

def foo5(a,b,c):
    print(a, b, c)
    time.sleep(2)

def goo():
    print('goo')
    time.sleep(3)

# * var get the all of positional args as tuple
# ** var get the all of keyward args as dict
# this operation is called perfect forwarding in cpp
def chron(f, *args, **kwargs):
    start = time.time()
    f(*args, **kwargs)
    end = time.time()
    print(f'elapsed: {end - start}')

chron(foo5, 1, 2, 3)
chron(foo5, 1, 2, c=3)

# packing >> when function is defined
# otherwise, unpacking
op = [4, 5, 6]
#hoo(op) # >> error
hoo(*op) # >> hoo(1, 2, 3)



# --------------------------------------------
import sys

# function is instance
# def add(x, y):
def add(x : int, y : int) -> int:     #: int >> anootations
    return x + y

# when you define a function, a obj called PyFunctioinObject is generated
# and check PyCodeOnject
print(hex(id(add)))
print(sys.getrefcount(add))
print(sys.getsizeof(add))

f = add
f(1, 2)


# the attributes of function obj
def foo(a= 10, b= 20, *, c=30, d=40):
    '''
        explaination of foo function
    '''

print(foo.__doc__)
print(foo.__name__)         # the name of function
print(foo.__qualname__)     # flsName.funcName
print(foo.__defaults__)
print(foo.__kwdefaults__)

print(add.__annotations__)
#help(add)


print('-'*30)
def outer(x):
    y = 0
    print(hex(id(x)), hex(id(y)))

    def inner():
        nonlocal x, y
        x = 10

    return inner

f = outer(10)
print(f.__closure__)    # the outer var of closure(inner func)

def foo1():
    print('foo')

print(foo.__dict__)

foo.__dict__['x'] = 10
foo.y = 20              #foo.__dict__['y'] = 20

print(foo.__dict__)

def goo():
    print('goo')

foo.goo = goo
foo.goo()


# user-defined func vs built-in func
print(add.__dict__)
# print(print.__dict__)     built-in func is optimized by c, they don have dict

print(add)
print(print)

print(sys.getsizeof(add))
print(sys.getsizeof(print))

print(dir(add))
print(dir(print))

print('-'*30, 'default params')
# default params
# because s is mutable type, so error below is raised
# so never use mutable type, or use None
# def add_sharp(s=[]):
#     s.append('#')
#     return s
def add_sharp(s=None):
    if s is None:
        s = []
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


# Python's default arguments are evaluated once when the function is defined, 
# not each time the function is called (like it is in say, Ruby). 
# This means that if you use a mutable default argument and mutate it, 
# you will and have mutated that object for all future calls to the function as well.
