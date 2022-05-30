class Point:
    # 인스턴스 필드는 객체의 __dict__에 저장
    #   __dict__을 사용시 외부에서 멤버를 자유롭게 추가 가능
    #   하지만 메모리 사용량이 많다.

    # __slots__을 사용시 x, y가 별도의 항목으로 저장
    #   외부에서 필드 추가 못함
    #   __dict__, __weekref__ 사라짐
    __slots__ = ['x', 'y']
    def __init__(self, x, y) -> None:
        self.x = x
        self._y = y

    # getter, setter를 적용하기 위해 property라는 것을 사용
    @property
    def y(self):
        print("print y")
        return self._y

    @y.setter
    def y(self, y):
        if y < 0:
            raise ValueError("wrong input")
        self._y = y


p1 = Point(1, 2)
#p1.z = 100

# p1.y = 5
# p2 = Point(3, -4)

print(dir(p1))
