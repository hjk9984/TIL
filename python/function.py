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
