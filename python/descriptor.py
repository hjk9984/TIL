# descriptor
# __get__, __set__,  __delete__ 중 한 개 이상의 메소드를 제공하는 클래스
# descriptor타입의 static feild 접근 시 __get__, __set__ 메소드가 자동으로 호출

class LogData:
    def __get__(self, obj, objType=None):
        print('__get__')
        return obj._y
    
    def __set__(self, obj, value):
        print('__set__')
        obj._y = value

# Sample 타입 객체의 __dict__에 x,y가 있고
# Sample 인스턴스의 __dict__에는 아무것도 없다.
class Sample:
    # static field
    x = 10
    y = LogData()   # static field로 만든 경우만 동작

    # initialization?
    # def __init__(self):
    #     self._y = 0

# n1 = Sample.x
# n2 = Sample.y   #Sample.y.__get__(...)

# print(type(n1))
# print(type(n2))

# Sample.y = 3.4    # var y points float obj not descriptor instance



print('-'*30)
#-----------------------------
sam1 = Sample()
# n5 = sam1.y  # 객체 이름으로 접근 가능,  read는 Sample 타입 객체의 __dict__에 접근 가능

print(Sample.__dict__)
print(sam1.__dict__)

sam1.x = 20      # writer
print(sam1.__dict__)

sam1.y = 100         # 객체의 __dict__ 에 y를 추가하지 않고 sam1.y.__set__호출
print(sam1.__dict__)
n = sam1.y           # sam1.y.__get__ 호출



print('-'*30)
#-----------------------------
sam2 = Sample()

#obj._y를 통해서 인스턴스 객체의 dict에 _y라는 객체가 생김
sam1.y = 50     # sam1.y.__set__(sam1.y, sam1, 20)
sam2.y = 70     # sam2.y.__set__(sam2.y, sam2, 20)

print(sam1.x)   # 필드 x를 직접 접근
print(sam1.y)   # __get__ 통해서 sam1._y
print(sam2.y)   

# sam1.y는 getter/setter를 통해서 _y 인스턴스 필드에 접근

sam3 = Sample()
print(sam3.y)
