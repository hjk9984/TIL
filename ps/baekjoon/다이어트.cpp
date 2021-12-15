//골드 4
//https://www.acmicpc.net/problem/1484

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

#define ll long long
#define endl "\n"

ll arr[50005];
int G;

int main(){
    ios::sync_with_stdio(false);
    cout.tie(0);

    cin >> G;

    vector<int> v;
    int bound = G/2 + 1;
    int s=1, e=1;

    for(int i=1; i<=bound; i++)
        arr[i] = pow(i, 2);

    while(e <= bound && s <= bound){
        //cout << s << " " << e << endl;
        int tmp = arr[e] - arr[s];
        if(tmp < G) e++;
        else if(tmp > G) s++;
        else {
            v.push_back(e);
            s++;
        }
    }

    if(v.empty()) cout << -1 << endl;
    else{
        for(auto e : v)
            cout << e << endl;
    }

}