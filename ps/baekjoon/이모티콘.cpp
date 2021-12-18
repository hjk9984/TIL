// gold 5
// https://www.acmicpc.net/problem/14226

// return s개의 이모티콘을 보내는데 걸리는 시간의 최솟값

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int S;
int arr[1005];

struct state{
    int n, c, s;    //num, clip, sec
};

int bfs(){
    state init = {1, 0, 0};
    queue<state> q;
    q.push(init);
    arr[1] = 0;
    
    while(!q.empty()){      //조건 확인하기
        int n = q.front().n;
        int c = q.front().c;
        int s = q.front().s;
        q.pop();

        if(n == S) return s;

        // display to clip
        if(s <= arr[n]) q.push({n, n, s+1});

        // clip to display
        if(c != 0 && n+c <= 1000){
            if(arr[n+c] > s+1)
                arr[n+c] = s+1;
            q.push({n+c, c, s+1});
        }

        // delete one emoji
        if(n >= 2){
            if(arr[n-1] > s+1)
                arr[n-1] = s+1;
            q.push({n-1, c, s+1});
        }
    }
    return 0;
}


#define INF 0x3f3f3f3f
#include <bits/stdc++.h>
int d[2222][2222];
int n;
// dp 풀이
// https://degurii.tistory.com/162

// 1) clip 변경
// 2) 실제 개수를 하나 삭제
// 3) 실제 개수를 clip 만큼 증가
int go(int clip, int screen) {
    if (screen > 2 * n || clip > 2 * n) return INF;
    if (screen < 0) return INF;
    if (screen == n) return 0;

    int &ret = d[clip][screen];
    if (ret != -1) return ret;
    ret = INF;
    ret = min(ret, go(screen, screen) + 1);
    ret = min(ret, go(clip, screen - 1) + 1);
    ret = min(ret, go(clip, screen + clip) + 1);
    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    memset(d, -1, sizeof(d));
    cin >> n;
    cout << go(0, 1);
}



int main(){
    cin >> S;

    for(int i=0; i<1005; i++) arr[i] = 123456789;
    int ans = bfs();

    cout << ans;
}