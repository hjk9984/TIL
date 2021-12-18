//silver 3
//https://www.acmicpc.net/problem/2579

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;
int arr[10001];
int dp[10001][2] = {};

int sol(int step, int con){
    if(step < 0) return 0;
    if(dp[step][con] > 0) return dp[step][con];
    
    int &ret = dp[step][con];
    if(con == 0){
        ret = max(sol(step-2, 0) + arr[step], sol(step-2, 1) + arr[step]);
    }
    else if(step > 0){
        ret = sol(step-1, 0) + arr[step];
    }
    
    return dp[step][con];
}


int main(){
    cin >> N;
    for(int i=0; i<N; i++){
        cin >> arr[i];
        //dp[i][0] = -1; dp[i][1] = -1;
    }
    
    int ans1 = sol(N-1, 0);
    int ans2 = sol(N-1, 1);
    
    cout << max(ans1, ans2);
}