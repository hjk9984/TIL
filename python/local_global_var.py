from tkinter import Y


x = 0
y = 0

def foo():
    global y
    global z
    x = 20      # generate local var
    y = 20
    z = 20      # generate global var
    print(x)
    print(y)

print('local', x)
print('local', y)
# print(z)

foo()

print(x)
print(y)
print(z)

print('-'*30)
gx = 1
def outer(ox):
    oy = 3

    # inner function
    def inner():
        global gx
        nonlocal ox     #not global, not local
        gx = 10
        ox = 10
        oy = 10
    
    def check():
        print(gx, ox, oy)
    
    return inner, check

f1, f2 = outer(2)

f1()
f2()
