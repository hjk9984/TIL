// gold 4
// 크게 만들기(https://www.acmicpc.net/problem/2812)

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
// input number dosent start with '0'

// I didnt think outline of solution before implementation
// so, it took many time to debugging

int N, K;
std::string ans;

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);
    std::cout.tie(0);

    std::cin >> N >> K;

    //initialization
    int idx = 0, cnt = 0;
    char tmp;
    std::cin >> tmp;
    ans += tmp;

    while (idx + cnt < N - 1)
    {
        std::cin >> tmp;

        if (tmp <= ans[idx] || cnt >= K)
        {
            ans += tmp;
            idx++;
        }
        else
        {
            ans[idx] = tmp;
            cnt++;

            while (idx > 0 && cnt < K)
            {
                if (ans[idx] <= ans[idx - 1])
                    break;

                ans[idx - 1] = ans[idx];
                ans.pop_back();
                idx--;
                cnt++;
            }
        }
    }
    std::cout << ans.substr(0, N - K);
}