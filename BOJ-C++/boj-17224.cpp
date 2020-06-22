#include <iostream>
#include <algorithm>
using namespace std;
int level[2];
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int N, L, K;
	cin >> N >> L >> K;
	for (int i = 0; i < N; i++) {
		int sub1, sub2;
		cin >> sub1 >> sub2;
		if (sub2 <= L)
			level[0]++;
		else if (sub1 <= L)
			level[1]++;
	}
	cout << 140 * min(K, level[0]) + 100 * min(K - level[0], level[1]);
}