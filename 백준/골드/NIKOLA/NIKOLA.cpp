// https://www.acmicpc.net/problem/2976

#include <iostream>
#include <climits>
#include <tuple>

using namespace std;


int main() {
    int i, j, n, result = INT_MAX;
    int cost[1005], dp[1005][1005]; // dp[점프거리][현재 발판 번호]

    // input
    cin >> n;

    for (i=1; i<=n; i++) {
        cin >> cost[i];
    }


    // init
    for (i=1; i<=n; i++) {
        for (j=1; j<=n; j++) {
            dp[i][j] = INT_MAX;
        }
    }
    dp[1][2] = cost[2];


    // dp
    for (i=1; i<=n; i++) {
        result = min(result, dp[i][n]);

        // 뒤로 점프가 있으므로 오른쪽 부터 처리해야됨 (왼쪽 부터 하다간 오른쪽에서 최소값 갱신이 될수 있어서)
        for (j=n-1; j>0; j--) {
            //  굳이 더 큰 값을 확인 할 필요 없으니.
            if (dp[i][j] < result) {

                // 뒤로 점프
                if (j - i > 0) {
                    dp[i][j-i] = min(dp[i][j-i], dp[i][j] + cost[j-i]);
                }

                // 앞으로 점프
                if (j + i < n) {  // j + i + 1 <= n
                    dp[i+1][j+i+1] = min(dp[i+1][j+i+1], dp[i][j] + cost[j+i+1]);
                }
            }
        }
    }


    // output
    cout << result;

    return 0;
}