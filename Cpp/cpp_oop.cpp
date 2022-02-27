#include <iostream>
#include <string>

class Point
{
    int x, y;

    // private 영역에 들어가면 호출이 안됨
    //~Point(){}

  public:
    Point() : x(0), y(0)
    {
        std::cout << "Point()" << std::endl;
    }

    Point(int a, int b) : x(a), y(b)
    {
        std::cout << "Point(int, int)" << std::endl;
    }

    ~Point()
    {
        std::cout << "~Point()" << std::endl;
    }

    Point(const Point &p) : x(p.x), y(p.y)
    {
        std::cout << "Point(const Point&)" << std::endl;
    }
};

class Reck
{
    // 멤버 생성자 호출 다음, 자신의 생성자가 호출
    Point p;

  public:
    Reck()
    {
        std::cout << "Rect()" << std::endl;
    }
};

void foo(Point p)
{
    ;
}

Point p1;
Point hoo()
{
    return p1;
}

Point koo()
{
    // Point p2(1, 2);  //  생성자 호출
    // return p2;       // 복사 생성자 호출

    return Point(1, 2);
}

int main()
{
    // Point p1[2];
    // Point p2[2] = {
    //     Point(0, 0),
    // };

    // Reck r;

    // 복사 생성자가 호출되는 경우
    // 1. 객체를 만들 때 자신의 타입으로 초기화 되는 경우 호출
    Point tmp1;
    Point tmp2(tmp1);

    // 2. call by value
    foo(tmp1);

    // 3. return by value
    hoo();
}
