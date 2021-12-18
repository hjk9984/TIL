// platinum 3
// https://www.acmicpc.net/problem/16930
// return 도착점에 도착하는 최소 시간

#include <iostream>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

#define f first
#define s second
#define INF 0x3f3f3f

int N, M, K;
char arr[1005][1005];
int dp[1005][1005];
bool visited[1005][1005];
pair<int, int> start, finish;

int dr[4] = {0, 1, 0, -1};
int dc[4] = {1, 0, -1, 0};

bool is_valid(const int &r, const int &c){
    return r >= 1 && r <= N && c >= 1 && c<= M;
}

int bfs(){
    queue<pair<int, int>> q;
    q.push(start);
    dp[start.f][start.s] = 0;

    while(!q.empty()){
        int r = q.front().f;
        int c = q.front().s;
        int sec = dp[r][c];
        q.pop();

        for(int j=0; j<4; j++){
            for(int i=1; i<=K; i++){
                int nr = r + dr[j]*i;
                int nc = c + dc[j]*i;

                if(nr == finish.f && nc == finish.s) return sec + 1;

                if(!is_valid(nr, nc)) break;
                if(arr[nr][nc] == '#') break;
                if(dp[nr][nc] == INF){
                    dp[nr][nc] = sec + 1;
                    q.push({nr, nc});
                }
                else if (dp[nr][nc] == sec + 1) continue;
                else break;
                //cout << nr << " " << nc << " " << sec+1 << endl;
            }
        }
    }

    return -1;

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M >> K;
    for(int i=1; i<=N; i++){
        for(int j=1; j<=M; j++){
            cin >> arr[i][j];
            dp[i][j] = INF;
        }
    }

    int r, c;
    cin >> r >> c;
    start = {r, c};
    cin >> r >> c;
    finish = {r, c};

    int ans = bfs();

    cout << ans;
}