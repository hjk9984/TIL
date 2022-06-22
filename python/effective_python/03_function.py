from effectice_python.utils import newline


# bw20 raise exception rather than return None
def careful_divide(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

result = careful_divide(1, 0)
if result is None:
    print("wrong1")

# None인지 검사하는 대신 빈 값을 False로 취급하는 검사를 실행할 수 있음 
if not result:      
    print("wrong2")


# 그럴 바에는 아래의 함수가 낫다
def careful_divide2(a, b):
    # assert statement raises an error when the condition is false.
    assert b != 0, "b is expected to be not zero"
    return a / b

def careful_divide3(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('wrong input')

# careful_divide2(1, 0)


# bw21
newline('bw21')
# 클로저 : 자신이 정의된 영역 ㅏㅂㄲ의 변수를 참조하는 함수
def sort_priority(numbers, group):
    found = False
    def helper(x):
        nonlocal found      # nonlocal은 왠만하면 쓰지 말기(간단한 함수에서만 사용)
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

# 함수가 복잡해지면 callable사용하는 게 낫다.
class sorter:
    def __init__(self, group):
        self.found = False
        self.group = group

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)

nums = [1, 3, 5, 6, 7] 
found = sort_priority(nums, [5, 6])
print(f"found? {found}")
print(nums)

nums.sort(key=sorter([2, 6]))
print(nums)


#bw22
newline('bw22')
def log(msg, *var):     # 가변인자 때문에 var를 안 넣어줘도 됨
    if not var:
        print(msg)
    else:
        var_str = ', '.join(str(v) for v in var)
        print(f"{msg} : {var_str}")

log('hi')#, [])

# 가변인자의 문제점
#   1.함수에 전달되기 전에 항상 튜플로 전환
#   만약 제네레이터를 받으면 모든 원소를 얻기 위해 반복 >> 메모리 소요
#   가변인수를 사용할 때는 인자의 개수가 충분히 작다는 것을 인지한 경우!

#   2. 새로운 위치 인자를 추가하면 해당 함수를 호출하는 모든 코드를 변경해야함
#   가변인자를 사용한 함수는 키워드 기반의 인자만 사용해서 확장!
def log(seq, msg, *var):
    if not var:
        print(msg)
    else:
        var_str = ', '.join(str(v) for v in var)
        print(f"{msg} : {var_str}")
#log('hi')  에러 발생!


# bw23
newline('bw23')
# 키워드 인자의 유연성
#   1. 디폴트 값을 지정할 수 있다
#   2. 하위 호환성을 제공하면서 함수 파라미터를 확장할 수 있다.
def flow_rate(weight_diff, time_diff):
    return weight_diff / time_diff

def flow_rate2(weight_diff, time_diff, period=1, units_per_kg=1):
    return ((weight_diff * units_per_kg) / time_diff) * period

# 하지만 period같은 선택적인 키워드 인자를 여전히 위치 인자로 지정할 수 있다.
flow_rate2(2, 3, 4, 5)

def flow_rate3(weight_diff, time_diff, *, period=1, units_per_kg=1):
    return ((weight_diff * units_per_kg) / time_diff) * period

try:
    flow_rate3(2, 3, 4, 5) #*를 이용해서 키워드 인자를 강제할 수 있다.
except TypeError as e:
    print(e)


# bw24
newline('bw24')
# 키워드 인자값이 정적으로 정해지는 타입을 쓰지 않을 때 디폴트 값으로 쓰면 X
from cmath import inf
from time import time
def log_t(msg, when=time()):
    print(f'{msg} : {when}')
log_t('hi')
log_t('hi2')
# 함수가 정의되는 시점에 time이 단 함번만 호출되기 때문에 항상 같다.

# 이런 동적으로 할당해야하는 디폴트 값의 경우 None을 쓴다
def log_t2(msg, when=None):
    if when is None:
        when = time()
    print(f'{msg} : {when}')
log_t2('2 hi')
log_t2('2 hi2')


# bw25
newline('bw25')
def safe_divide(a, b, *, ignore_overflow=False, ignore_zero_division=False):
    try:
        return a / b
    except ZeroDivisionError as e:
        if ignore_zero_division:
            return 0
        raise ValueError(e)
    except OverflowError as e:
        if ignore_overflow:
            return inf
        raise ValueError(e)

# safe_divide(1, 0)
safe_divide(a=1, b=2)   # 키워드도 되고 위치 인자도 가능 

def safe_divide2(a, b, /, *, ignore_overflow=False, ignore_zero_division=False):
    try:
        return a / b
    except ZeroDivisionError as e:
        if ignore_zero_division:
            return 0
        raise ValueError(e)
    except OverflowError as e:
        if ignore_overflow:
            return inf
        raise ValueError(e)

#safe_divide2(a=1, b=2) >> /으로 인해서 에러 발생
