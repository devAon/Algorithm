#include <iostream>
using namespace std;
int main() {
	int n, m, result = 0, sum = 0, end = 0;
	int data[30000] = {};
	cin >> n >> m;
	for (int i = 0; i < n; i++)
		cin >> data[i];
	for (int start = 0; start < n; start++) {
		while (sum < m && end < n) {
			sum += data[end];
			end++;
		}
		if (sum == m) result++;
		sum -= data[start];
	}
	cout << result;
	return 0;
}
