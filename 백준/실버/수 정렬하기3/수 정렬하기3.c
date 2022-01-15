// https://www.acmicpc.net/problem/10989

#include<stdio.h>

int main() {
    int i, n, tmp;
    int arr[10005] = {0,};

    scanf("%d", &n);
    for (i=0; i < n; i++) {
        scanf(" %d", &tmp);
        arr[tmp]++;
    }

    for (i=0; i < 10005; i++) {
        while (arr[i]--) {
            printf("%d\n", i);
        }
    }
    
    return 0;
}
