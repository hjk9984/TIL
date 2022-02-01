#include <iostream>
#include <vector>
#include <algorithm>

class flower
{
    static const int dates[12];

public:
    //const int s, e;
    // const를 이용하면 sort안의 swap으로 인해서 에러 발생
    // swap(a, b) >> ...; a.e = b.e >> error
    int s, e;
    flower(const int *arr) : s(dates[arr[0] - 1] + arr[1]), e(dates[arr[2] - 1] + arr[3]) {}

    bool operator<(const flower &f)
    {
        return this->s < f.s;
    }
};

const int flower::dates[12] = {0, 31, 59, 90, 120,
                               151, 181, 212, 243,
                               273, 304, 334};
// dates를 관리하는 struct를 가지고

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);
    std::cin.tie(0);

    int N, n1, n2;
    int arr[4];
    std::vector<flower> v;

    std::cin >> N;
    for (int i = 0; i < N; i++)
    {
        std::cin >> arr[0] >> arr[1] >> arr[2] >> arr[3];
        v.push_back(flower(arr));
    }

    sort(v.begin(), v.end());

    //greedy
    int selected = 0;
    int cur = 60, deadline = 60;
    for (int i = 0; i < N; i++)
    {
        if (v[i].s > deadline) //빈틈
        {
            selected = 0;
            break;
        }

        if (v[i].s > cur)
        {
            cur = deadline;
            selected++;
        }

        if (v[i].e > 334) // 도착하면 나오기
        {
            deadline = v[i].e;
            selected++;
            break;
        }

        deadline = std::max(v[i].e, deadline);
    }

    if (deadline > 334)
        std::cout << selected << std::endl;
    else
        std::cout << 0 << std::endl;
}