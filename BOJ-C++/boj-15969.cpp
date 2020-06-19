#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main() {
	int n, temp;
	vector<int> v;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> temp;
		v.push_back(temp);
	}
	sort(v.begin(), v.end());
	cout << v[n - 1] - v[0];

	return 0;
}