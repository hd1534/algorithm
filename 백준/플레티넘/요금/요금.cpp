// https://www.acmicpc.net/problem/1140

#include <iostream>

using namespace std;

#define DEFAULT_PRICE 10

int main() {
    long long tmp, iter_count, result;
    long long t, k1, k2, p1, p2, n1, n2, nd;
    double p1_per_text, p2_per_text;

    cin >> t >> k1 >> p1 >> k2 >> p2;

    p1_per_text = (double)p1 / k1;
    p2_per_text = (double)p2 / k2;

    // 더 저렴한걸 p1으로
    if (p1_per_text > p2_per_text) {
        swap(p1, p2);
        swap(k1, k2);
        swap(p1_per_text, p2_per_text);
    }

    // 최대 10
    if (p1_per_text > DEFAULT_PRICE) {
        k1 = 1;
        p1 = DEFAULT_PRICE;
        p1_per_text = DEFAULT_PRICE;
    }
    if (p2_per_text > DEFAULT_PRICE) {
        k2 = 1;
        p2 = DEFAULT_PRICE;
        p2_per_text = DEFAULT_PRICE;
    }


    // cout << p1_per_text << ' ' << p2_per_text << ' ' << (k1 / abs(k1 - k2) + 1) << endl;

    // n1, n2: 팩 개수.  nd: 기본값으로 계산할 개수
    nd = 1;  // to skip first 'nd != 0' condition
    n1 = t / k1;
    long long remainder = t % k1;
    result = (n1 + 1) * p1;  // 1번째 팩을 넉넉하게 하나 더 구매한 경우

    iter_count = k1 == k2 ? 1 : (k1 / abs(k1 - k2) + 5);  // 뭔가 느낌상 이정도만 반복하면 될 것 같은데
    // 1번째 팩을 하나씩 적게 사고 나머지를 2번 팩과 기본값으로 채워보는 반복문
    for (long long i = 0; i <= iter_count && nd != 0; i++) {
        tmp = i * k1 + remainder;

        n2 = tmp / k2;
        nd = tmp % k2;
        //        2번째 팩을 넉넉하게 하나 더 산 경우.   나머지는 그냥 기본값을 낸 경우      
        tmp = min(p1 * (n1 - i) + p2 * (n2 + 1), p1 * (n1 - i) + p2 * n2 + DEFAULT_PRICE * nd);

        result = min(result, tmp);
    }


    cout << result << endl;

    return 0;
}