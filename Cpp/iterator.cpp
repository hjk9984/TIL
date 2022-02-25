#include <iostream>
#include <list>
#include <vector>
using namespace std;

int main()
{
    vector<int> v = {1, 2, 3, 4, 5};
    list<int> l = {1, 2, 3, 4, 5};
    int arr[5] = {1, 2, 3, 4, 5};

    // 반복자 사용하기
    vector<int>::iterator iter1 = v.begin();
    auto iter2 = v.begin();
    auto iter3 = begin(v); // 이걸 통해   배열도 반복자 사용 가능

    auto iter4 = begin(arr);
    while (iter4 != end(arr))
        cout << *iter4++ << " ";
    cout << endl;

    auto iter5 = rbegin(arr);
    while (iter5 != rend(arr))
        cout << *iter5++ << " ";
    cout << endl;

    cout << "--------------------------\n";
    auto iter6 = begin(l);
    // cout << *(iter6 + 2);     임의 접근이 안되서 불가능
    while (iter6 != end(l))
        cout << *iter6++ << " ";
    cout << endl;
}
