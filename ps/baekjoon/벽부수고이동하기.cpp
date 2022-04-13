// https://www.acmicpc.net/problem/2206

#include <iostream>
#include <queue>
#include <string>
#include <vector>
using namespace std;

char arr[1001][1001];
bool visited[2][1001][1001];
int N, M;
int dr[4] = {0, 1, 0, -1};
int dc[4] = {1, 0, -1, 0};
int ans = -1;

struct state
{
    int r, c, m;
    bool crushed;
};

void bfs()
{
    queue<state> q;
    q.push({0, 0, 1, false});
    visited[0][0][0] = true;

    while (!q.empty())
    {
        int r = q.front().r;
        int c = q.front().c;
        int m = q.front().m;
        bool crushed = q.front().crushed;
        q.pop();

        if (r == N - 1 && c == M - 1)
        {
            ans = m;
            return;
        }

        for (int i = 0; i < 4; i++)
        {
            int nr = r + dr[i];
            int nc = c + dc[i];

            if (nr < 0 || nr >= N || nc < 0 || nc >= M)
                continue;
            if (visited[crushed][nr][nc])
                continue;

            if (arr[nr][nc] == '1' && (!crushed))
            {
                visited[1][nr][nc] = 1;
                q.push({nr, nc, m + 1, 1});
            }

            if (arr[nr][nc] == '1')
                continue;

            visited[crushed][nr][nc] = 1;
            q.push({nr, nc, m + 1, crushed});
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    string tmp;

    cin >> N >> M;
    for (int i = 0; i < N; i++)
    {
        cin >> tmp;
        for (int j = 0; j < M; j++)
        {
            arr[i][j] = tmp[j];
        }
    }

    bfs();
    cout << ans;
}
