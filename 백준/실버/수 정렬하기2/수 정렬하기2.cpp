// https://www.acmicpc.net/problem/2751

#include<stdio.h>
#include<algorithm>

// time over 최악의 경우가 케이스에 있는 듯
// 합병정렬, 힙 정렬을 쓰거나 여기에 median of median 적용하거나 인듯
/// 가장 간단한 오름차순 퀵정렬
// void quickSort(int *start, int *end) {
//     int tmp;
//     int *h, *t;

//     if (start >= end) {
//         return;
//     }

//     h = start + 1; t = end;

//     while (1) {
//         // 맨 왼쪽을 피봇으로 선택
//         while (*h < *start) h++;
//         while (*t > *start) t--;

//         if (h < t) {
//             tmp = *h; *h = *t; *t = tmp;
//         }
//         else {
//             break;
//         }
//     }

//     tmp = *start; *start = *t; *t = tmp;

//     quickSort(start, t-1);
//     quickSort(t+1, end);
// }

using namespace std;

int main() {
    int n;
    int i,j,k;
    int arr[1000005];

    scanf("%d", &n);
    for (i=0; i < n; i++) {
        scanf(" %d", arr+i);
    }

    sort(arr, arr + n);
    
    for (i=0; i < n; i++) {
        printf("%d\n", arr[i]);
    }

    return 0;
}
