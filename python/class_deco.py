class add_emoticon:
    def __init__(self, emoticon):
        self.emoticon = emoticon

    def __call__(self, func):
        self.func = func
        def inner(*args, **kwargs):
            print(self.emoticon, end='')
            return self.func(*args, **kwargs)
        
        return inner

    # def __init__(self, func):
    #     self.func = func

    # def __call__(self, *args, **kwargs):
    #     print("XD ", end='')
    #     return self.func(*args, **kwargs)
    # discriptor without args

# @add_emoticon       # say_hi = add_emoticon(say_hi)
@add_emoticon(">< ") # say_hi = add_emoticon(><)(say_hi)
def say_hi(name):
    print(f'hi, {name}!')

say_hi('kim')
print(type(say_hi))


# callable obj
#   ()을 사용해서 호출 가능한 객체
#   내장함수 callable을 사용해서 확인가능

n = 10
print(callable(print))  # 내장함수
print(callable(n))      # int
print(callable(int))    # type
