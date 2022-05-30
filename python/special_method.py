class Sentence:
    def __init__(self, s):
        self.words = s.split()

    
    # special method
    # __xxx__ 형태의 메소드
    # 파이썬 표준 타입과 유사하데 동작하는 클래스를 설계하기 위해서 반드시 필요
    def __len__(self):
        return len(self.words)

    def __getitem__(self, idx):
        return self.words[idx]

    # 객체의 상태를 문자열로 보여줌
    # 이 함수가 없으면 __repr__을 호출
    def __str__(self):
        return " ".join(self.words)
    
    # 디버깅 등 내부적인 용도
    def __repr__(self):
        return " ".join(self.words)

    # NotIMplemented 확실히 알아둘 것
    def __add__(self, other):
        if isinstance(other, Sentence):
            return Sentence( " ".join(self.words + other.words))
        elif isinstance(other, str):
            return Sentence( " ".join(self.words) + other)
        else:    
            return NotImplemented

    def __iadd__(self, other):
        print("__iadd__ oper")
    
    def __radd__(self, other):
        print("__radd__ oper")

s1 = Sentence("i am a boy")
s2 = Sentence("i am a girl")
print(len(s1))
print(s1[2])
print(s1)
print(s1.__len__())
print(s1.__repr__())

print(repr(s1))
print(str(s1))

s3 = s1 + s2    # s1.__add__(s2)
print(s3)
print(s1)
print(id(s1))

s4 = s1 + "aa"
print(s4)
print(s1)
print(id(s1))
# s1 += 'AA'      

#'AA' + s1  # s1.__radd__('AA') or str.__add__
# return NotImplemented 이 있어야  s1.__radd__('AA')를 사용 



# callable object
class Plus:
    def __call__(self, x, y):
        return x + y
    

p = Plus()
n2 = p(1, 2)
