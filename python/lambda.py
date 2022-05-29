s1 = ['banana', 'kiwi', 'apple']

print(sorted(s1, key=lambda x:len(x)))
print(sorted(s1, key=len))
print(sorted(s1, key=lambda x : x[::-1]))
print(s1[0][-1])


def add1(x, y):
    return x+y

add2 = lambda x, y : x+y
print(type(add1))
print(type(add2))

print(add1)
print(add2)

# lambda func is similar to normal func
add2.__dict__['x'] = 100
print(add2.x)


x = 10

# important
f1 = lambda y : x+y         # 실행시 x평가
f2 = lambda y, x=x : x+y    # 이 순간 x 평가

x=20

print(f1(1))
print(f2(1))

f3 = lambda x, y: x if x> y else y
print(f3(10, 5))
print(f3(6, 8))
