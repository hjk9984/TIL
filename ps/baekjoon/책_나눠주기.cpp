// gold 1
// https://www.acmicpc.net/problem/9576

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

int T, N, M;
bool visited[1005];

class Student
{
public:
    int s, e;
    Student(int a, int b) : s(a), e(b) {}
    bool operator<(const Student &st) const
    {
        if (this->e == st.e)
        {
            return this->s < st.s;
        }
        else
        {
            return this->e < st.e;
        }
    }
};

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);
    std::cout.tie(0);

    std::cin >> T;
    for (int i = 0; i < T; i++) //while(T--)
    {
        std::vector<Student> v;
        std::cin >> N >> M;
        int a, b;
        for (int j = 0; j < M; j++)
        {
            std::cin >> a >> b;
            v.push_back(Student(a, b));
        }

        sort(v.begin(), v.end());

        int cnt = 0;
        for (int j = 0; j < M; j++)
        {
            for (int k = v[j].s; k <= v[j].e; k++)
            {
                if (visited[k])
                    continue;
                else
                {
                    visited[k] = true;
                    cnt++;
                    break;
                }
            }
        }
        std::cout << cnt << std::endl;
        //visit init
        memset(visited, 0, sizeof(visited));
    }
}