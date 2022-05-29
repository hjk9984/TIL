# first class obj
#  can be param of func
#       return val of func
#       할당 명령문의 대상
#       동일 비교의 대상

# int, str obj are first class obj
# in python, func is first class obj too.

def foo():
    print('foo')

f = foo
print(f == foo)

def f1(f):
    f()

f1(foo)

def f2():
    return foo

f2()()
