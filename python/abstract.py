from abc import ABC, abstractmethod

# 추상 클래스를 상속받아서 추상 클래스가 됨
class Shape(ABC):
    @abstractmethod
    def Draw(self):
        pass

class Rect(Shape):
    def Draw(self):
        pass

r = Rect()
# s = Shape()   Can't instantiate abstract class Shape with abstract method Draw
