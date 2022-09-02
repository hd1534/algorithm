// https://www.acmicpc.net/problem/9019
// 틀림...

#include<queue>
#include<string>
#include<iostream>


using namespace std;


// d1 = n / 1000;
// d2 = n / 100 % 10;
// d3 = n / 10 % 10;
// d4 = n % 10;

inline int D(int n) {
    return (n*2)%10000;
}

inline int S(int n ) {
    return n-1 < 0 ? 9999 : n-1;
}

inline int L(int n ) {
    return n / 100 % 10 * 1000 + n / 10 % 10 * 100 + n % 10 * 10 + n / 1000;
}

inline int R(int n ) {
    return n % 10 * 1000 + n / 1000 * 100 + n / 100 % 10 * 10 + n / 10 % 10;
}


string bfs() {
    int  target, cur, next;
    string arr[10000] = {"",};

    queue<int> q;

    cin>>cur;
    cin>>target;

    q.push(cur);
    while (!q.empty()) {
        cur = q.front();
        q.pop();

        if (cur == target)
            return arr[target];

        if (!arr[next = D(cur)].size()) {
            arr[next] = arr[cur] + "D";
            q.push(next);
        }

        if (!arr[next = S(cur)].size()) {
            arr[next] = arr[cur] + "S";
            q.push(next);
        }

        if (!arr[next = L(cur)].size()) {
            arr[next] = arr[cur] + "L";
            q.push(next);
        }

        if (!arr[next = R(cur)].size()) {
            arr[next] = arr[cur] + "R";
            q.push(next);
        }
    }
    

    return "";
}


int main(){
    int n;


    cin>>n;
    while (n--) {
        cout << bfs() << endl;
    }


    return 0;
}