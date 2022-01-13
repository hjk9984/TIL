//return 광고의 최적의 시작 위치 (누적 재생시간이 가장 터야함)
//여러 곳이라면 가장 빠른 시작 시각 리턴

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <queue>
using namespace std;

#define ll long long

int ad[360000];

int stot(string str){
    int hour = stoi(str.substr(0, 2));
    int min = stoi(str.substr(3, 5));
    int sec = stoi(str.substr(6, 8));

    return hour*3600 + min*60 +sec;
}

string tost(int time){
    string res = "";
    int s = time%60;
    time /= 60;
    int m = time%60;
    time /= 60;
    int h = time;

    if(h<10) res+="0";
    res+=to_string(h);
    res+=":";

    if(m<10) res+="0";
    res+=to_string(m);
    res+=":";

    if(s<10) res+="0";
    res+=to_string(s);

    return res;

}


string solution(string play_time, string adv_time, vector<string> logs) {
    string answer = "";
    int adv = stot(adv_time);
    int play = stot(play_time);
    ll max_time = 0, sum = 0;
    int idx = 0;

    for(auto &e : logs){
        int start = stot(e.substr(0, 8));
        int end = stot(e.substr(9, 8));
        for(int i=start; i<end; i++) ad[i]++;
    }
    
    queue<int> q;

    for(int i=0; i<adv; i++){
        sum += ad[i];
        q.push(ad[i]);
    }
    max_time = sum;

    for(int i=adv; i<play;i++){
        sum += ad[i];
        q.push(ad[i]);
        sum -= q.front();
        q.pop();
        if(sum > max_time){
            idx = i-adv+1;
            max_time = sum;
        }
    }


    return answer;
}