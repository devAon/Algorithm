#include <iostream>
#include <algorithm>
using namespace std;
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	int n; cin >> n;
	int arr[n] = { 0 };
	for (int i = 0; i < n; i++)
		cin >> arr[i];

	sort(arr, arr + n);

	int m; cin >> m;
	for (int i = 0; i < m; i++) {
		int x; cin >> x;
		cout << (binary_search(arr, arr + n, x) ? "1\n" : "0\n");

	}
	return 0;
}