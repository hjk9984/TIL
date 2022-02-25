#include <iostream>
#include <stdio.h>
namespace xtd
{
class ostream
{
  public:
    ostream &operator<<(int n)
    {
        printf("%d", n);
        return *this;
    }
    ostream &operator<<(double n)
    {
        printf("%f", n);
        return *this;
    }
    ostream &operator<<(char c)
    {
        printf("%c", c);
        return *this;
    }

    ostream &operator<<(ostream &(*f)(ostream &))
    {
        (*f)(*this);
        return *this;
    }
};
ostream cout;
ostream &endl(ostream &os)
{
    os << '\n';
    return os;
}
// ostream &(*f)(ostream &)setw(int k, char c)
// {
//     ostream &func(ostream & os)
//     {
//         while (k--)
//             os << c;
//         return os;
//     }
//     return &func;
// }
} // namespace xtd

class Point
{
    int x, y;

  public:
    Point(int x, int y) : x(x), y(y)
    {
    }

    friend std::ostream &operator<<(std::ostream &os, const Point &p);
};

std::ostream &operator<<(std::ostream &os, const Point &p)
{
    os << p.x << " " << p.y;
    return os;
}

// 연산자 재정의할때 멤버 함수와 일반 함수 중에 하나만 써야함
// 우선순위는 멤버 함수가 일반 함수보다 높아 둘다 같이 있으면 멤버함수가 쓰인다.
// 상태가 변하면 멤버 함수를 쓰고 그렇지 않는 경우 일반 함수를 쓴다.

class Integer
{
    int value;

  public:
    Integer(int n = 0) : value(n)
    {
    }
    void print() const
    {
        std::cout << value << std::endl;
    }

    friend std::ostream &operator<<(std::ostream &, const Integer &);

    // prefix
    Integer &operator++()
    {
        ++value;
        return *this;
    }

    // postfix
    Integer operator++(int)
    {
        Integer tmp = *this;
        ++value;
        return tmp;
    }
};

std::ostream &operator<<(std::ostream &os, const Integer &k)
{
    os << k.value;
    return os;
}

class xtring
{
    char *str;
    int size;

  public:
    xtring(const char *k)
    {
        size = strlen(k);
        str = new char[size + 1];
        memcpy(str, k, size);
    }
    ~xtring()
    {
        delete[] str;
    }

    // 대입 연산자는 포인터가 멤버 데이터 중에 존재하면
    // 동적으로 처리를 해줘야 한다.
    // 컴파일러는 이런 대입 연산자가 없으면 알아서 만들어 준다.
    xtring &operator=(const xtring &s)
    {
        size = s.size;
        delete[] str;
        str = new char[size + 1];
        // 같은 클래스이지만 다른 객체의 private을 접근?
        // https://stackoverflow.com/questions/6921185/why-do-objects-of-the-same-class-have-access-to-each-others-private-data
        memcpy(str, s.str, size);
        return *this;
    }

    friend std::ostream &operator<<(std::ostream &, const xtring &);
};

std::ostream &operator<<(std::ostream &os, const xtring &Str)
{
    os << Str.str;
    return os;
}

int main()
{
    xtd::cout << 5 << ' ' << 3.14 << xtd::endl;

    Point tmp(1, 2);
    std::cout << tmp << '\n';

    Integer tmp1;
    std::cout << tmp1++ << std::endl;
    std::cout << tmp1 << std::endl;

    xtring tmp2 = "hihi";
    std::cout << tmp2 << std::endl;
    xtring tmp3 = "kim";
    tmp2 = tmp3;
    std::cout << tmp2 << std::endl;
}
